# from playwright.sync_api import sync_playwright

# # 需要添加的请求头
# def checkFromPlaywright():
#     headers = {
#             "Cookie": "WMSS=47cf961761aee1d044c850514942663f; wmuid=5641; langue=zh; fp=77c4132c42f2391b5aadbac67ec42ef4; token=or6NUAYDfh5E1H7Ng3V1Q4vi1qy6cYSutbREGZOAGkTb7/T+pYuoQH4652hsboz4wlMtypEWdLdHrZROnpRLIg==; WNJWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJ3YWltYW81MTgiLCJhdWQiOiIiLCJpYXQiOjE3MjEzMjA2NzcsIm5iZiI6MTcyMTMyMDY3OSwiZXhwIjoxNzIzOTEyNjc3LCJkYXRhIjp7ImlkIjo1NjQxLCJ1c2VybmFtZSI6IjQ4NDY1MiIsImZvb3RwcmludCI6Ijc3YzQxMzJjNDJmMjM5MWI1YWFkYmFjNjdlYzQyZWY0IiwiaG9zdCI6IndhaW1hbzUxOCJ9fQ.cLFSohF7FrhGNaXzwa9yS83KJ9bQWhnYys7KnJxqWKLP5m5xdxjaUCtGVJoszu_TOr_UKq8NjxX1pag0MQe91g; cf_clearance=J3062I0.HDgiUwMNjsrBTQKP217dUby2mzFWNxaFlq8-1721750607-1.0.1.1-5E0tc0DvVSCmV0dP_1FopK.oHjPsxj22D3bhPh8eouZyBl6u0rS3YMGgOlqZ_qdqmtgKDjGF2kvVK6taX8rOlQ",
#             'Cache-Control': 'max-age=0',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
#             'Xmode': 'navigate',
#             'Sec-Fetch-Site': 'same-origin',
#             'Sec-Fetch-Mode': 'cors',
#             'Sec-Fetch-Dest': 'empty',
#             'Accept-Encoding': 'gzip, deflate',
#             'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#             'If-Modified-Since': 'Mon, 22 Jul 2024 15:38:05 GMT',
#             'Priority': 'u=1, i'
#         }
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
        
#         # 设置请求头
#         for key, value in headers.items():
#             page.set_extra_http_headers({key: value})
        
#         page.goto("https://semrush5-zh.waimao518.com/analytics/overview/?searchType=domain&q=perplexity.ai")
        
#         browser.close()
