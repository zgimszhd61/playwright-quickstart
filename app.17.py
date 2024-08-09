from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    url = "https://s.taobao.com/search?_input_charset=utf-8&commend=all&ie=utf8&initiative_id=tbindexz_20170306&q=ai%20%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E&search_type=item&source=suggest&sourceId=tb.index&spm=a21bo.jianhua%2Fa.201856.d13&ssid=s5-e&suggest=history_1&suggest_query=&wq="
    page.goto(url,timeout=60000,wait_until='load')
    time.sleep(3)
    page.screenshot(path="example.png")
    browser.close()

