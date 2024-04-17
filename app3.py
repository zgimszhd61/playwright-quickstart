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

tryURL("https://twitter.com/Himalaya_bear1/status/1568366959405977601")
tryURL("https://twitter.com/urassholes/status/1770628393010430184")
tryURL("https://twitter.com/realliaohaibo/status/1763021229785796877")
tryURL("https://twitter.com/DottChen/status/1494216950054100993")
