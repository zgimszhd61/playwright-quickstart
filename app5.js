// 2024.05.26 :最终部署的版本.
const fs = require('fs').promises;
const { chromium } = require('playwright');
const NodeCache = require('node-cache');
const myCache = new NodeCache();

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
        await fs.appendFile(filename, content + "\n", { encoding: 'utf-8' });
    } catch (error) {
        console.error(`写入文件 ${filename} 时发生错误：${error.message}`);
    }
}

async function tryURL(content, murl) {
    const alltext = await read_file_content('answerwithpaper.txt');
    if (alltext && alltext.includes(content)) {
        return;
    }

    const browser = await chromium.launch();
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
    await write_to_file("answerwithpaper.txt", ariaLabelValue + " --- " + content);

    await browser.close();
}

(async () => {
    const linesContent = await fs.readFile('paper.txt', { encoding: 'utf-8' });
    const lines = linesContent.split('\n');
    for (const line of lines) {
        const parts = line.trim().split(" ---- ");
        await tryURL(parts[1], parts[0]);
    }
})();