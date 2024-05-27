const fs = require('fs').promises;
const { chromium } = require('playwright');
const NodeCache = require('node-cache');
const myCache = new NodeCache();
let allTexts = []; // 用于存储answerwithpaper.txt文件的内容

async function read_file_content(filename) {
    const cachedContent = myCache.get(filename);
    if (cachedContent) {
        return cachedContent;
    }

    try {
        const content = await fs.readFile(filename, { encoding: 'utf-8' });
        myCache.set(filename, content);
        return content;
    } catch (error) {
        console.error(`读取文件 ${filename} 时发生错误：${error.message}`);
        return null;
    }
}

async function write_to_file(filename, content) {
    try {
        await fs.appendFile(filename, content.join("\n") + "\n", { encoding: 'utf-8' }); // 一次性写入所有内容
    } catch (error) {
        console.error(`写入文件 ${filename} 时发生错误：${error.message}`);
    }
}

async function tryURL(browser, content, murl) {
    if (allTexts.includes(content)) {
        return;
    }

    const page = await browser.newPage();
    await page.goto(murl);
    await page.waitForSelector('article');
    const elementWithAriaLabel = await page.locator('article');
    let innerText = await elementWithAriaLabel.innerText();
    innerText = innerText.replace(/(\r\n|\r|\n)/g, " ");
    let ariaLabelValue = '';

    const years = ['2024', '2023', '2022'];
    for (const year of years) {
        if (innerText.includes(`, ${year}`)) {
            console.log(innerText);
            ariaLabelValue = `${year} ${innerText.split(`, ${year}`)[1].replace(/(\r\n|\r|\n)/g, " ")}`;
            break;
        }
    }

    console.log(ariaLabelValue);
    allTexts.push(ariaLabelValue + " --- " + content); // 将新内容添加到数组中

    await page.close();
}

(async () => {
    const browser = await chromium.launch(); // 在程序开始时创建浏览器实例
    const linesContent = await fs.readFile('paper.txt', { encoding: 'utf-8' });
    const lines = linesContent.split('\n');
    allTexts = (await fs.readFile('answerwithpaper.txt', { encoding: 'utf-8' })).split('\n'); // 一次性读取文件内容
    for (const line of lines) {
        const parts = line.trim().split(" ---- ");
        try{
            await tryURL(browser, parts[1], parts[0]);
        } catch (error) {
            console.error(`发生错误：${error.message}`);
        }

    }
    await write_to_file("answerwithpaper.txt", allTexts); // 在程序结束时一次性写入文件
    await browser.close(); // 关闭浏览器实例
})();