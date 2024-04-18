from playwright.sync_api import sync_playwright

def tryURL(murl):
  with sync_playwright() as p:
      browser = p.webkit.launch()
      page = browser.new_page()
      # page.goto("https://twitter.com/minglaugodel/status/1775573019768893784")
      page.goto(murl)
      element_with_aria_label = page.locator('article')

      # 获取aria-label属性的值
      try:
        if "· 2024年" in element_with_aria_label.inner_text():
          aria_label_value = "2024年" + element_with_aria_label.inner_text().split("· 2024年")[1].replace("\n"," ")
        if "· 2023年" in element_with_aria_label.inner_text():
          aria_label_value = "2023年" + element_with_aria_label.inner_text().split("· 2023年")[1].replace("\n"," ")
        if "· 2022年" in element_with_aria_label.inner_text():
          aria_label_value = "2022年" + element_with_aria_label.inner_text().split("· 2022年")[1].replace("\n"," ")
        print(aria_label_value)
      except:
        print("ERROR")
      page.screenshot(path="example.png")
      browser.close()


# 打开文件
with open('paper.txt', 'r') as file:
    for line in file:
        print("======")
        print(line.strip().split(" ---- ")[1])
        try:
            tryURL(line.strip().split(" ---- ")[0])
        except:
            print("ERROR")