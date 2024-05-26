const fs = require('fs').promises;
const { chromium } = require('playwright');
const NodeCache = require('node-cache');
const myCache = new NodeCache();

// 缓存读取文件内容的函数
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
        if (error.code === 'ENOENT') {
            console.log(`错误：文件 ${filename} 未找到。`);
        } else if (error.code === 'EIO') {
            console.log(`错误：读取文件 ${filename} 时发生IO错误。`);
        } else {
            console.log(`未知错误：${error.message}`);
        }
        return null;
    }
}

// 定义一个sleep函数
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 使用async函数来使用await调用sleep
async function demoSleep() {
    console.log('开始暂停');
    await sleep(1000); // 暂停2秒
    console.log('结束暂停');
}

// 将内容写入文件
async function write_to_file(filename, content) {
    try {
        await fs.appendFile(filename, content + "\n", { encoding: 'utf-8' });
    } catch (error) {
        console.error(`写入文件 ${filename} 时发生错误：${error.message}`);
    }
}

// 使用Playwright打开网页并处理内容
async function tryURL(content, murl) {
    alltext = await read_file_content('answerwithpaper.txt');
    if (alltext && alltext.includes(content)) {
        return;
    }
    try {
        browser = await chromium.launch();
        // 创建一个页面
        page = await browser.newPage();
        // 导航到一个网页
        await page.goto(murl);
        // 确保页面的特定元素加载完成
        await page.waitForSelector('article');
        // 定位到页面中的article元素
        elementWithAriaLabel = await page.locator('article');
        // 获取该元素的文本内容
        innerText = await elementWithAriaLabel.innerText();
        // await demoSleep();
        binnerTextb = await innerText.replace(/(\r\n|\r|\n)/g, " ");
        ariaLabelValue = '';
        if (binnerTextb.includes(', 2024')) {
            console.log(binnerTextb);
            ariaLabelValue = await '2024 ' + binnerTextb.split(', 2024')[1].replace(/(\r\n|\r|\n)/g, " ");
        }
        if (binnerTextb.includes(', 2023')) {
            console.log(binnerTextb);
            ariaLabelValue = await '2023 ' + binnerTextb.split(', 2023')[1].replace(/(\r\n|\r|\n)/g, " ");
        }
        if (binnerTextb.includes(', 2022')) {
            console.log(binnerTextb);
            ariaLabelValue = await '2022 ' + binnerTextb.split(', 2022')[1].replace(/(\r\n|\r|\n)/g, " ");
        }

        console.log(ariaLabelValue);
        if (ariaLabelValue.includes("K  Views")){
          await write_to_file("answerwithpaper.txt", ariaLabelValue + " --- " + content);
        }

        await browser.close();
    }catch (error) {
        console.error("An error occurred while reading the file:", error.message);
    }
}

(async () => {
    const alltext = await read_file_content('answerwithpaper.txt');
    console.log(alltext);

    const linesContent = await fs.readFile('paper.txt', { encoding: 'utf-8' });
    const lines = linesContent.split('\n');
    for (const line of lines) {
        console.log("======");
        const parts = line.trim().split(" ---- ");
        console.log(parts[1]);
        await tryURL(parts[1], parts[0]);
    }
})();