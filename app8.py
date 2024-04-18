



from playwright.sync_api import sync_playwright

def tryURL(murl):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto(murl)

        page.set_default_timeout(45000)  # 设置超时时间为45000毫秒

        # 使用 XPath 定位元素
        xpath_locator = page.locator('//*[@id="Main"]/div[2]/div[1]/small')

        # 尝试获取元素的文本内容
        try:
            text_content = xpath_locator.inner_text()
            print("Extracted text:", text_content)
        except Exception as e:
            print("Error extracting text:", str(e))

        # 截图保存
        page.screenshot(path="example.png")
        browser.close()


# 打开文件
with open('paper.txt', 'r') as file:
    for line in file:
        print("======")
        print(line.strip().split(" ---- ")[0])
        try:
            tryURL(line.strip().split(" ---- ")[1])
        except:
            print("ERROR")