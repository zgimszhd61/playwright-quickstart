const { chromium } = require('playwright');
const fs = require('fs');

async function tryURL(browser,murl) {
    const page = await browser.newPage();
    await page.goto(murl);

    // 设置超时时间为45000毫秒
    page.setDefaultTimeout(45000);

    // 使用 XPath 定位元素
    const xpathLocator = '//*[@id="Main"]/div[2]/div[1]/small';

    // 尝试获取元素的文本内容
    try {
        const textContent = await page.locator(xpathLocator).innerText();
        console.log("Extracted text:", textContent);
    } catch (e) {
        console.log("Error extracting text:", e.message);
    }

    // 截图保存
    // await page.screenshot({ path: 'example.png' });
}

async function processFile() {
    // 读取文件
    const data = fs.readFileSync('paper.txt', 'utf8');
    const lines = data.split('\n');
    const browser = await chromium.launch(); // 在程序开始时创建浏览器实例

    for (const line of lines) {
        if (line.trim()) {
            const [label, url] = line.trim().split(' ---- ');
            console.log("======");
            console.log(label);
            try {
                await tryURL(browser,url);  // 等待每个 URL 处理完成
            } catch (error) {
                console.log("ERROR");
            }
        }
    }
    await browser.close();
}

// 调用处理文件的函数
processFile();
