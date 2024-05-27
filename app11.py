from playwright.async_api import async_playwright
import asyncio
import functools

# 使用lru_cache装饰器来缓存函数的结果
@functools.lru_cache(maxsize=None)  # maxsize=None 表示无限制缓存大小
def read_file_content(filename):
    """读取指定文件的全文内容并缓存结果"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 {filename} 未找到。")
        return None
    except IOError:
        print(f"错误：读取文件 {filename} 时发生IO错误。")
        return None
    except Exception as e:
        print(f"未知错误：{str(e)}")
        return None

async def tryURL(browser, content, murl,alltext):
    if content in alltext:
        return
    page = await browser.new_page()
    await page.goto(murl)
    element_with_aria_label = page.locator('article')
    aria_label_value = ""
    if "· 2024年" in await element_with_aria_label.inner_text():
        aria_label_value = "2024年" + (await element_with_aria_label.inner_text()).split("· 2024年")[1].replace("\n", " ")
    if "· 2023年" in await element_with_aria_label.inner_text():
        aria_label_value = "2023年" + (await element_with_aria_label.inner_text()).split("· 2023年")[1].replace("\n", " ")
    if "· 2022年" in await element_with_aria_label.inner_text():
        aria_label_value = "2022年" + (await element_with_aria_label.inner_text()).split("· 2022年")[1].replace("\n", " ")
    print(aria_label_value)
    write_to_file("answerwithpaper.txt", aria_label_value + " --- " + content)
    await page.close()

def write_to_file(filename, content):
    with open(filename, 'a+', encoding='utf-8') as file:
        file.writelines(content + "\n")

async def main():
    async with async_playwright() as p:
        browser = await p.webkit.launch()
        alltext = read_file_content('answerwithpaper.txt')
        with open('paper.txt', 'r') as file:
            for line in file:
                content = line.strip().split(" ---- ")[1]
                murl = line.strip().split(" ---- ")[0]
                try:
                    await tryURL(browser, content, murl,alltext)
                except:
                    print("ERROR")
        await browser.close()

asyncio.run(main())