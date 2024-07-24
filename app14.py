from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Headers for the request
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': os.environ.get("COOKIE"),
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

def fetch_website_data(page, keyword):
    url = f"https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key={keyword}"
    xpath = '//*[@id="react-app"]/div/div[4]/div[2]/div[2]/span/div/div/span/div[3]/div[2]/section/div/section/div[2]/div/div[1]/div[3]/div[1]/div[3]'
    xpath_rate = '//*[@id="react-app"]/div/div[4]/div[2]/div[2]/span/div/div/span/div[3]/div[2]/section/div/section/div[2]/div/div[1]/div[3]/div[1]/div[4]/div[1]/div/span[2]'
    if content_exists_in_file(keyword):
        print("===={} has exists , so ignore.".format(keyword))
        return
    try:
        page.set_extra_http_headers(headers)
        page.goto(url)
        page.wait_for_timeout(5000)  # 等待页面加载
        content = page.locator(xpath).text_content()
        rate = page.locator(xpath_rate).text_content()
        print(f"{keyword} == {content} == {rate}")
        write_to_file(f"{keyword} == {content} == {rate}",keyword)
    except Exception as e:
        logging.error(f"ERROR for {keyword}: {e}")

def write_to_file(content,keyword):
    with open('SimillarwebContent.txt', 'a+', encoding='utf-8') as file:
            file.write(content + "\n")

## 判断是否存在，如果存在就不用重复记录了.
def content_exists_in_file(content):
    try:
        with open('SimillarwebContent.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
            return content in file_content
    except FileNotFoundError:
        # 如果文件不存在，返回False
        return False
    
def main(keywords):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        for keyword in keywords:
            fetch_website_data(page, keyword)
        browser.close()

if __name__ == "__main__":
    keywords = [
        "perplexity.ai", 
        "scite.ai",
        "shadcn.com",
        "moonshot.cn",
        "you.com",
        "cloudinary.com",
        "gptstore.ai",
        "vercel.com",
        "supabase.com",
        "typeform.com",
        
        ]
    main(keywords)
