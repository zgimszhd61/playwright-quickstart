from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost:64122/?q=%E4%BD%A0%E5%A5%BD")
    page.screenshot(path="example.png")
    browser.close()

