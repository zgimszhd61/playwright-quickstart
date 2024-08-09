from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    # url = "https://item.taobao.com/item.htm?spm=a21n57.1.item.4.4df77de4WvrOz7&priceTId=2147817a17221585761097589e4ed1&utparam=%7B%22aplus_abtest%22:%22836a7475598f13ec90fbb80acae2be26%22%7D&id=662265575950&ns=1&abbucket=4"
    # url2 = "https://jp.shein.com/FRIFUL-Women-s-Plant-Printed-Tie-Front-Short-Sleeve-Shirt-p-30763447.html?src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_1%60ps%3D3_1%60jc%3Dreal_2030&src_module=All&src_tab_page_id=page_home1722158843020&mallCode=1&pageListType=4&imgRatio=3-4"
    url3 = "https://x.com/FengShuiPapers"
    page.goto(url3,timeout=60000,wait_until='load')
    time.sleep(3)
    page.screenshot(path="example.png")
    browser.close()

