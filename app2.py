from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    # page.goto("https://twitter.com/minglaugodel/status/1775573019768893784")
    page.goto("https://twitter.com/crypto_chanshi/status/1698623548179558833")
    # 使用包含特定文本的选择器定位元素
    # 获取页面上所有文本内容

    # 定位到具有特定aria-label属性的元素
    element_with_aria_label = page.locator('article')

    # 获取aria-label属性的值
    try:
      if "· 2024年" in element_with_aria_label.inner_text():
        aria_label_value = "2024年" + element_with_aria_label.inner_text().split("· 2024年")[1].replace("\n"," ")
      if "· 2023年" in element_with_aria_label.inner_text():
        aria_label_value = "2023年" + element_with_aria_label.inner_text().split("· 2023年")[1].replace("\n"," ")
    except:
      print("ERROR")
    print(aria_label_value)
    page.screenshot(path="example.png")
    browser.close()
