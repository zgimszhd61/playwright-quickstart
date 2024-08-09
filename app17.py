from playwright.sync_api import sync_playwright
from openai import OpenAI
import os,re
import time
from dotenv import load_dotenv

load_dotenv()

def extract_content(url, selector):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()
        page.goto(url)
        # time.sleep(2)
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
    print("checking {}".format(keyword))
    # url1 = "https://www.google.com.hk/search?q={}+site%3Aai&newwindow=1&sca_esv=b2c38071ce043d54&hl=zh-CN&sxsrf=ADLYWIL1F1I7QXuoER7U_zVoH71YXGGNNg%3A1721745257334&ei=ab-fZriIFKXc2roP6q2x6QI&ved=0ahUKEwj44NPzsL2HAxUlrlYBHepWLC0Q4dUDCA8&uact=5&oq=assistant+site%3Aai&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWFzc2lzdGFudCBzaXRlOmFpSMaNAVDkBFiPiwFwEHgBkAEBmAGQBKABwjGqAQwwLjI2LjMuMC4xLjK4AQPIAQD4AQGYAgWgAvEHwgIKEAAYsAMY1gQYR8ICBBAjGCfCAgoQIxiABBgnGIoFwgIFEAAYgATCAhAQLhiABBjRAxhDGMcBGIoFwgILEC4YgAQY0QMYxwHCAhAQLhiABBjRAxjHARgKGMsBwgIIEAAYgAQYywGYAwCIBgGQBgeSBwUxLjEuM6AH9kw&sclient=gws-wiz-serp".format(keyword)
    # url2 = "https://www.google.com.hk/search?q={}+site:ai&newwindow=1&sca_esv=b2c38071ce043d54&hl=zh-CN&sxsrf=ADLYWIKIfxRwR-0R65VKSOWFeHifa_QSbg:1721745278035&ei=fr-fZq3lAdGq0-kP46Xo4AY&start=10&sa=N&sstk=Aagrsuj3BXnZeqPtlSqpK-dL9VzXFJOIjMMMW5xIAJmis7A9debXehf1xG8jsacHljR85Fwjb4R9upOgpU_8uXK5VhvaOG5jZ86OmQ&ved=2ahUKEwitnMP9sL2HAxVR1TQHHeMSGmwQ8tMDegQIDBAE&biw=1057&bih=883&dpr=2".format(keyword)
    try:
        url1 = "https://www.google.com/search?q={}&newwindow=1&sca_esv=b2c38071ce043d54&hl=zh-CN&sxsrf=ADLYWIL1F1I7QXuoER7U_zVoH71YXGGNNg%3A1721745257334&ei=ab-fZriIFKXc2roP6q2x6QI&ved=0ahUKEwj44NPzsL2HAxUlrlYBHepWLC0Q4dUDCA8&uact=5&oq=assistant+site%3Aai&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWFzc2lzdGFudCBzaXRlOmFpSMaNAVDkBFiPiwFwEHgBkAEBmAGQBKABwjGqAQwwLjI2LjMuMC4xLjK4AQPIAQD4AQGYAgWgAvEHwgIKEAAYsAMY1gQYR8ICBBAjGCfCAgoQIxiABBgnGIoFwgIFEAAYgATCAhAQLhiABBjRAxhDGMcBGIoFwgILEC4YgAQY0QMYxwHCAhAQLhiABBjRAxjHARgKGMsBwgIIEAAYgAQYywGYAwCIBgGQBgeSBwUxLjEuM6AH9kw&sclient=gws-wiz-serp".format(keyword)
        url2 = "https://www.google.com/search?q={}&newwindow=1&sca_esv=b2c38071ce043d54&hl=zh-CN&sxsrf=ADLYWIKIfxRwR-0R65VKSOWFeHifa_QSbg:1721745278035&ei=fr-fZq3lAdGq0-kP46Xo4AY&start=10&sa=N&sstk=Aagrsuj3BXnZeqPtlSqpK-dL9VzXFJOIjMMMW5xIAJmis7A9debXehf1xG8jsacHljR85Fwjb4R9upOgpU_8uXK5VhvaOG5jZ86OmQ&ved=2ahUKEwitnMP9sL2HAxVR1TQHHeMSGmwQ8tMDegQIDBAE&biw=1057&bih=883&dpr=2".format(keyword)


        selector = '//*[@id="rso"]/div//div/div/div[1]/div/div/span/a/div/div/div/div[2]/cite'

        content1 = extract_content(url1, selector)
        content2 = extract_content(url2, selector)
        # print(content1)
        # print(content2)
        for item in content1:
            content = "{} , {}".format(item.split(" ")[0],keyword)
            print(content)
            write_to_file(content)

        for item in content2:
            content = "{} , {}".format(item.split(" ")[0],keyword)
            print(content)
            write_to_file(content)
    except:
        print("ERROR occur ...")


def askGPT(question):
    client = OpenAI()
    precontent = """接下来我将给你一个词语，请为我提供英文语境下这个词语的其他10种同义词,同义词之间用','隔开，不要说其他内容-----------"""
    # precontent = """使用最简单的表达方式，用中文重新表达下面内容，不要用英语回答-----------"""
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                'role': 'user',
                "content": precontent + question,
            },
        ]
    )
    result = completion.choices[0].message.content
    print(result)
    return(result)


def askAndSearch(domain):
    mlist = askGPT(domain).split(",")
    for item in mlist:
        main("{} site:ai".format(item.strip()))

# askAndSearch("阅读")
# askAndSearch("写作")
# askAndSearch("教育")
# askAndSearch("医疗")
# askAndSearch("法律")
# askAndSearch("社交")
# askAndSearch("情感陪伴")


# askAndSearch("游戏")
# askAndSearch("插画")
# askAndSearch("会议纪要")
# askAndSearch("日程安排")
# askAndSearch("相亲")
# askAndSearch("招聘")
# askAndSearch("心理学")
# askAndSearch("小说")
# askAndSearch("历史")
# askAndSearch("同城活动")
# askAndSearch("虚构")
# askAndSearch("企业服务")
# askAndSearch("营销服务")


# askAndSearch("声音克隆")

# askAndSearch("电影")
# askAndSearch("综艺")

askAndSearch("笔记")
# askAndSearch("电子商务")
# askAndSearch("推荐")
# askAndSearch("素材")
# askAndSearch("saas服务")
# askAndSearch("漏洞")
# askAndSearch("喜欢")
# askAndSearch("爱情")
# askAndSearch("校园")
# askAndSearch("分享")
# askAndSearch("扫描")
# askAndSearch("总结")
# askAndSearch("摘要")
# askAndSearch("邮件")
# askAndSearch("新闻")
# askAndSearch("时间")
# askAndSearch("硬件")
# askAndSearch("眼镜")
# askAndSearch("戒指")
# askAndSearch("项链")
# askAndSearch("宠物")
# askAndSearch("识别")
# askAndSearch("检测")
# askAndSearch("推广")
# askAndSearch("约会")
# askAndSearch("crm")
# askAndSearch("erp")
# askAndSearch("面试")
# askAndSearch("应聘")
# askAndSearch("医药")
# askAndSearch("基因")
# askAndSearch("未来")
# askAndSearch("论文阅读")
# askAndSearch("朋友")
# askAndSearch("珠宝")
# askAndSearch("文案")
# askAndSearch("财报")
# askAndSearch("金融")
# askAndSearch("商品推荐")
# askAndSearch("新闻聚合")
# askAndSearch("产品试用")
# askAndSearch("杯子")
# askAndSearch("留言")
# askAndSearch("聊天")
# askAndSearch("创业")
# askAndSearch("销售")
# askAndSearch("模拟")

# main("assistant")
# main("companion")

# main("music")
# main("ai generate")
# main("ai write")
# main("video")

# main("learning")
# main("conpanion")
# main("task")

# main("travel")
# main("girl friend")
# main("knowledge")

# main("tool")
# main("game")
# main("hang zhou")
# main("数学")
# main("孙子兵法")
# main("三国演义")

# main("金瓶梅")
# main("西游记")

# main("孙中山")
# main("曾国藩")

# main("红楼梦")

# main("undress ai")
# main("taylor swift ai")
# main("alaya ai")
# main("joyland ai")
# main("candy ai")
# main("nudify ai")
# main("hotpot ai")

# main("rizz ai")
# main("starry ai")

# main("talk dirty ai")
# main("veggie ai")
# main("ai answer generator")
# main("event site:ai")

# main("story site:ai")
# main("clone site:ai")

# main("meet site:ai")
# main("game site:ai")
# main("business site:ai")
# main("dog site:ai")
# main("girl friend site:ai")
# main("boy friend site:ai")
# main("hotel site:ai")
# main("movie site:ai")
# main("crm site:ai")
# main("oa site:ai")
# main("paas site:ai")
# main("saas site:ai")

# main("Recompose site:ai")
# 以ai为种子搜索词.
# 以shadcn为种子搜索词.

# main("news site:ai")
