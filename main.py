import requests
from bs4 import BeautifulSoup
import time

'''
    填入自己的Cookie
'''
base_headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "xn--pxtr7m5ny.com",
    "Pragma": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": ""
}

'''
    将获取到的文章链接放入 links
'''
links = []

'''
    记得补全 base_headers["Referer"]
'''
for each_link in links:
    url = each_link
    base_headers["Referer"] = f" "
    r = requests.get(url, headers=base_headers)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    container = soup.find('div', {'class': 'post-body'}).find('span').findAll('p')
    title = soup.find('div',{'class':"col-xs-12"}).find('div',{'class':'text-center'}).find('strong').get_text()
    f = open("test.txt", "a")
    print(title)
    f.write(title)
    f.write('\n')
    for line in container:
        f.write(line.get_text())
        f.write('\n')
    f.close()
    time.sleep(5)