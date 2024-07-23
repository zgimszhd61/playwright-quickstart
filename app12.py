from playwright.sync_api import sync_playwright

def extract_links(page,key):
    # 使用XPath提取包含href属性的元素
    elements = page.locator('xpath=//div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div//div/div[1]/h3/div//a').all()
    elements_stars = page.locator('xpath=//div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div//div/div[1]/ul//a').all()
    elements_langs = page.locator('xpath=//div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div/div[1]/ul/li[1]/span').all()


    try:
        for i in range(0,len(elements)):
            url = "github.com/{}".format(elements[i].get_attribute('href'))
            starNum = elements_stars[i].inner_text().strip()
            lang = elements_langs[i].inner_text().strip()
            content = "{} , {} , {}".format(url , starNum , lang)
            write_to_file(content,key)
    except:
        print("ERROR:{}".format(url))


def write_to_file(content,key):
    if content_exists_in_file(content):
        print("{} has exists , so ignore.".format(content))
        return
    else:
        with open('content.txt', 'a+', encoding='utf-8') as file:
            file.write(content + " , " + key + "\n")

## 判断是否存在，如果存在就不用重复记录了.
def content_exists_in_file(content):
    try:
        with open('content.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
            return content in file_content
    except FileNotFoundError:
        # 如果文件不存在，返回False
        return False

def doSearch(page,key,num):
    # 访问第一页
    page.goto("https://github.com/search?q={}+language%3A*&type=repositories&s=stars&o=desc&p={}".format(key,num))
    # extract_links(page,key)
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
# SearchKeywordFromGithub("spider")
# SearchKeywordFromGithub("write")
# SearchKeywordFromGithub("swiftui")
# SearchKeywordFromGithub("agent")
# SearchKeywordFromGithub("shadcn")
SearchKeywordFromGithub("next")
SearchKeywordFromGithub("nuxt")
SearchKeywordFromGithub("image")
SearchKeywordFromGithub("machine learning")
SearchKeywordFromGithub("reinforcement learning")