import urllib
import json
import codecs
from urllib import request
from bs4 import BeautifulSoup


def get_soup_from_keyword(keyword="笔记本电脑", page=1):
    """
    根据keyword & page 获取 content
    """
    # page处理 京东
    url = "https://search.jd.com/Search?"
    page = 2 * page-1
    params = {'keyword': keyword, 'enc': 'utf-8', 'page': page}
    data = urllib.parse.urlencode(params)
    htmlUrl = url+data
    req = urllib.request.Request(htmlUrl)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")

    # print(html)
    file = codecs.open("html.html", 'w+', 'utf-8')
    file.write(html)
    file.close()
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    return soup


"""
page=2n-1
https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&page=5
"""


if __name__ == "__main__":
    soup = get_soup_from_keyword(keyword="笔记本电脑", page=4)
    li_s = soup.find_all('li', class_="gl-item")
    print(len(li_s))

    res = []
    i = 0
    for li in li_s:
        i = i+1
        data = {}
        data['id'] = i
        data['sku'] = li['data-sku']
        data['price'] = li.find(class_='p-price').select('i')[0].string
        des = li.find(class_='p-name').select('em')[0].strings
        data['name'] = next(des)
        next(des)
        data['configuration'] = next(des)
        res.append(data)

    for i in res:
        print(i)
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
