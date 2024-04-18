from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://chat.openai.com/chat")

    # 使用Playwright填充输入框并提交问题
    page.query_selector("#prompt-textarea").fill("告诉我，你的知识库截止日期是？")
    page.wait_for_selector('button[data-testid="send-button"]').click()
    time.sleep(2)
    print(page.url)

    ## TODO：待解决，保留登陆态，并且能够从后台导出数据.
   
    browser.close()

with sync_playwright() as playwright:
    run(playwright)