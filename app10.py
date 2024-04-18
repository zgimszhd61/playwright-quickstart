# TODO: 查询google，并且//*[@id="rso"]//h3. 就可以节省surpdev的钱.

from playwright.sync_api import sync_playwright
import time

def tryURL(murl):
  with sync_playwright() as p:
      browser = p.webkit.launch()
      page = browser.new_page()
      page.goto(murl)
      page.screenshot(path="example.png")
      time.sleep(3)
      browser.close()


tryURL("https://www.google.com.hk/search?q=nihao&newwindow=1&sca_esv=63c115a30e488880&hl=zh-CN&sxsrf=ACQVn0-eH7ArVrcQGzenuKTNDCu9i1aPcA%3A1713436326443&source=hp&ei=pvYgZs3gGKbc2roP7rWuKA&iflsig=ANes7DEAAAAAZiEEtgTtk07qO1Zf5yn05DYieGaO66hP&ved=0ahUKEwjNy9Lcx8uFAxUmrlYBHe6aCwUQ4dUDCBU&uact=5&oq=nihao&gs_lp=Egdnd3Mtd2l6IgVuaWhhbzIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIKEC4YgAQYChjLATIIEAAYgAQYywEyBRAAGIAEMgUQLhiABDIFEAAYgAQyBRAuGIAEMgUQABiABEj2EVC7AljqDnADeACQAQCYAbABoAHPCaoBAzAuOLgBA8gBAPgBAZgCC6AC-QmoAgrCAgcQIxgnGOoCwgIKECMYgAQYJxiKBcICCxAuGIAEGNEDGMcBwgIHEAAYgAQYCsICBxAuGIAEGArCAgoQABiABBgKGMsBwgIQEC4YgAQY0QMYxwEYChjLAcICCBAuGIAEGNQCmAMJkgcDMy44oAfXXA&sclient=gws-wiz")