from playwright.sync_api import sync_playwright

def extract_links(page,key):
    # 使用XPath提取包含href属性的元素
    elements = page.locator('xpath=//div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div//div/div[1]/h3/div//a').all()

    for link in elements:
        # 获取href属性
        href = link.get_attribute('href')
        url = "github.com/{}".format(href)
        write_to_file(url,key)


def write_to_file(content,key):
    with open('content.txt', 'a+', encoding='utf-8') as file:
        file.write(content + " , " + key + "\n")

def doSearch(page,key,num):
    # 访问第一页
    page.goto("https://github.com/search?q={}&type=repositories&s=stars&o=desc&p={}".format(key,num))
    extract_links(page,key)
    page.screenshot(path="example{}.png".format(num))


def SearchKeywordFromGithub(key):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        doSearch(page,key,1)
        doSearch(page,key,2)
        browser.close()

# SearchKeywordFromGithub("gpt")
SearchKeywordFromGithub("spider")
SearchKeywordFromGithub("write")
SearchKeywordFromGithub("swiftui")
SearchKeywordFromGithub("agent")
SearchKeywordFromGithub("openai")

