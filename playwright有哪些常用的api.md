# playwright有哪些常用的api

Playwright提供了一系列强大的API，用于自动化浏览器操作和测试。以下是一些常用的Playwright API：

1. **页面导航和加载**：
   - `page.goto(url)`: 导航到指定的URL。
   - `page.reload()`: 重新加载当前页面。
   - `page.waitForNavigation()`: 等待页面导航事件完成。

2. **元素交互**：
   - `page.click(selector)`: 点击页面上的元素。
   - `page.fill(selector, value)`: 填充输入框或文本区域。
   - `page.press(selector, key)`: 在指定元素上模拟按键操作。

3. **元素选择和获取信息**：
   - `page.$(selector)`: 返回页面上匹配指定选择器的第一个元素。
   - `page.$$(selector)`: 返回页面上匹配指定选择器的所有元素。
   - `page.textContent(selector)`: 获取元素的文本内容。
   - `page.getAttribute(selector, name)`: 获取元素的属性值。

4. **断言和验证**：
   - `expect(page).toHaveTitle(title)`: 验证页面标题是否符合预期。
   - `expect(page).toHaveURL(url)`: 验证当前页面的URL是否符合预期。

5. **截图和录制**：
   - `page.screenshot(options)`: 对当前页面进行截图。
   - `page.video()`: 获取页面的视频录制。

6. **网络请求和路由控制**：
   - `page.route(url, handler)`: 拦截网络请求并定义处理逻辑。
   - `page.request.post(url, options)`: 发送POST请求。

7. **设备模拟和视图控制**：
   - `page.setViewportSize(width, height)`: 设置页面视图大小。
   - `page.emulateMedia(features)`: 模拟媒体特性，如打印或屏幕媒体。

8. **上下文管理**：
   - `browser.newContext(options)`: 创建一个新的浏览器上下文。
   - `context.newPage()`: 在特定上下文中创建一个新页面。

这些API使得Playwright能够执行各种自动化任务，如表单填写、页面导航、元素点击、内容验证等。Playwright的API设计简洁而强大，支持所有主流浏览器，包括Chrome、Firefox、Safari等，并且支持移动端页面测试和Headless模式的测试[1][2][3][5].

Citations:
[1] https://cuiqingcai.com/36045.html
[2] https://cloud.tencent.com/developer/news/919289
[3] https://blog.testops.vip/2023/04/03/playwright/
[4] https://developer.aliyun.com/article/1174356
[5] https://www.cnblogs.com/NHB6870/p/17797857.html
