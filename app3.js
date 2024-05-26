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
    const alltext = await read_file_content('answerwithpaper.txt');
    if (alltext && alltext.includes(content)) {
        return;
    }

      const browser = await chromium.launch();
      // 创建一个页面
    const page = await browser.newPage();
      // 导航到一个网页
    await page.goto(murl);
    // 确保页面的特定元素加载完成
    await page.waitForSelector('article');
    // 定位到页面中的article元素
    const elementWithAriaLabel = await page.locator('article');
    // 获取该元素的文本内容
    const innerText = await elementWithAriaLabel.innerText();
    // 通过console.log打印出来
    console.log(innerText);

    // 关闭浏览器
    await browser.close();
    //const browser = await webkit.launch();
    //const page = await browser.newPage();
    //await page.goto(murl);
    //await page.waitForSelector('article');
    //const elementWithAriaLabel = await page.locator('article');
    //const innerText = await elementWithAriaLabel.innerText();

    //let ariaLabelValue = '';
    //if (innerText.includes('· 2024年')) {
    //    ariaLabelValue = '2024年' + innerText.split('· 2024年')[1].replace("\n", " ");
    //}
    // Repeat for other years...

    //console.log(ariaLabelValue);
    //await write_to_file("answerwithpaper.txt", ariaLabelValue + " --- " + content);

    //await browser.close();
}

// 示例使用
(async () => {
    const alltext = await read_file_content('answerwithpaper.txt');
    console.log(alltext);

    const lines = await fs.readFile('paper.txt', { encoding: 'utf-8' });
    lines.split('\n').forEach(async (line) => {
        console.log("======");
        const parts = line.trim().split(" ---- ");
        console.log(parts[1]);
	await tryURL(parts[1], parts[0]);
    });
})();
