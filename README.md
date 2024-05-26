# playwright-quickstart
## 安装方法：
1.  在vultr之中选择ubuntu，不要选24.04版本（太新，playwright还不支持），选择22.04版本。
2. 安装后登陆，首先升级node版本及其配套(不然12版本node，playwright也不支持）。
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install node
npx playwright install
apt-get install libasound2
```
3. 编写demo程序，如下代码保存为app.js
```
const { chromium } = require('playwright');

(async () => {
  // 启动浏览器
  const browser = await chromium.launch();
  // 创建一个页面
  const page = await browser.newPage();
  // 导航到一个网页
  await page.goto('https://baidu.com');
  // 捕获页面的截图
  await page.screenshot({ path: `example.png` });
  // 关闭浏览器
  await browser.close();
})();
```
4. 运行app.js
```
node app.js
```

## 在后台运行的方法
```
nohup node bb6.js &
```