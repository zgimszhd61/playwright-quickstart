from playwright.sync_api import sync_playwright


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

# 示例使用
alltext = read_file_content('answerwithpaper.txt')


def tryURL(content,murl):
  ## 如果已经检查过了，就不用再检查.
  if content in alltext:
     return
  with sync_playwright() as p:
      browser = p.webkit.launch()
      page = browser.new_page()
      # page.goto("https://twitter.com/minglaugodel/status/1775573019768893784")
      page.goto(murl)
      element_with_aria_label = page.locator('article')

      # 获取aria-label属性的值
      try:
        if "· 2024年" in element_with_aria_label.inner_text():
          aria_label_value = "2024年" + element_with_aria_label.inner_text().split("· 2024年")[1].replace("\n"," ")
        if "· 2023年" in element_with_aria_label.inner_text():
          aria_label_value = "2023年" + element_with_aria_label.inner_text().split("· 2023年")[1].replace("\n"," ")
        if "· 2022年" in element_with_aria_label.inner_text():
          aria_label_value = "2022年" + element_with_aria_label.inner_text().split("· 2022年")[1].replace("\n"," ")
        if "· 2021年" in element_with_aria_label.inner_text():
          aria_label_value = "2021年" + element_with_aria_label.inner_text().split("· 2021年")[1].replace("\n"," ")
        print(aria_label_value)
        write_to_file("answerwithpaper.txt", aria_label_value + " --- " + content)
        
      except:
        print("ERROR")
      # page.screenshot(path="example.png")
      browser.close()

def write_to_file(filename, content):
    """
    将内容写入指定的文件。
    
    :param filename: str, 要写入的文件名
    :param content: str, 要写入的内容
    """
    # 使用'w'模式打开文件，如果文件不存在，将会被创建
    with open(filename, 'a+', encoding='utf-8') as file:
        file.writelines(content+"\n")  # 写入内容

# print(alltext)

# # 打开文件
with open('paper.txt', 'r') as file:
    for line in file:
        print("======")
        print(line.strip().split(" ---- ")[1])
        try:
            tryURL(line.strip().split(" ---- ")[1],line.strip().split(" ---- ")[0])
        except:
            print("ERROR")