from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://github.com/search?q=gpt&type=repositories&s=stars&o=desc&p=2")
    page.screenshot(path="example.png")
    browser.close()

