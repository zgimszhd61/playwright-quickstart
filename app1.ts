import { chromium, Page } from 'playwright';

(async () => {
  // 启动浏览器
  const browser = await chromium.launch();
  // 创建一个页面
  const page = await browser.newPage();
  // 导航到一个网页
  await page.goto('https://twitter.com/ALJVD1/status/1764317403108803036');
  
  // 确保页面的特定元素加载完成
  await page.waitForSelector('article');
  // 定位到页面中的article元素
  const elementWithAriaLabel = page.locator('article');
  // 获取该元素的文本内容
  const innerText = await elementWithAriaLabel.innerText();
  // 通过console.log打印出来
  console.log(innerText);
  
  // 关闭浏览器
  await browser.close();
})();