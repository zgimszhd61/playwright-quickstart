from playwright.sync_api import sync_playwright

def extract_content(url, selector):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.locator(selector).all_text_contents()
        browser.close()
        return content

def write_to_file(content):
    if content_exists_in_file(content):
        print("===={} has exists , so ignore.".format(content))
        return
    else:
        with open('SearchEngineContent.txt', 'a+', encoding='utf-8') as file:
            file.write(content + "\n")

## 判断是否存在，如果存在就不用重复记录了.
def content_exists_in_file(content):
    try:
        with open('SearchEngineContent.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
            return content in file_content
    except FileNotFoundError:
        # 如果文件不存在，返回False
        return False

def main(keyword):

    url1 = "https://www.google.com.hk/search?q={}+site%3Aai&newwindow=1&sca_esv=b2c38071ce043d54&hl=zh-CN&sxsrf=ADLYWIL1F1I7QXuoER7U_zVoH71YXGGNNg%3A1721745257334&ei=ab-fZriIFKXc2roP6q2x6QI&ved=0ahUKEwj44NPzsL2HAxUlrlYBHepWLC0Q4dUDCA8&uact=5&oq=assistant+site%3Aai&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWFzc2lzdGFudCBzaXRlOmFpSMaNAVDkBFiPiwFwEHgBkAEBmAGQBKABwjGqAQwwLjI2LjMuMC4xLjK4AQPIAQD4AQGYAgWgAvEHwgIKEAAYsAMY1gQYR8ICBBAjGCfCAgoQIxiABBgnGIoFwgIFEAAYgATCAhAQLhiABBjRAxhDGMcBGIoFwgILEC4YgAQY0QMYxwHCAhAQLhiABBjRAxjHARgKGMsBwgIIEAAYgAQYywGYAwCIBgGQBgeSBwUxLjEuM6AH9kw&sclient=gws-wiz-serp".format(keyword)
    url2 = "https://www.google.com.hk/search?q={}+site:ai&newwindow=1&sca_esv=b2c38071ce043d54&hl=zh-CN&sxsrf=ADLYWIKIfxRwR-0R65VKSOWFeHifa_QSbg:1721745278035&ei=fr-fZq3lAdGq0-kP46Xo4AY&start=10&sa=N&sstk=Aagrsuj3BXnZeqPtlSqpK-dL9VzXFJOIjMMMW5xIAJmis7A9debXehf1xG8jsacHljR85Fwjb4R9upOgpU_8uXK5VhvaOG5jZ86OmQ&ved=2ahUKEwitnMP9sL2HAxVR1TQHHeMSGmwQ8tMDegQIDBAE&biw=1057&bih=883&dpr=2".format(keyword)

    selector = '//*[@id="rso"]/div//div/div/div[1]/div/div/span/a/div/div/div/div[2]/cite'

    content1 = extract_content(url1, selector)
    content2 = extract_content(url2, selector)

    for item in content1:
        content = "{} , {}".format(item.split(" ")[0],keyword)
        print(content)
        write_to_file(content)

    for item in content2:
        content = "{} , {}".format(item.split(" ")[0],keyword)
        print(content)
        write_to_file(content)

# main("assistant")
# main("companion")

# main("music")
# main("ai generate")
# main("ai write")
# main("video")

# main("learning")
# main("conpanion")
# main("task")

main("travel")
main("girl friend")
main("knowledge")
