# 常用框架

## 插入图片

``` html
<div align=center>
<hr>
xxx
<hr>
</div>
```

## 网页解析

``` python
from urllib import request
from bs4 import BeautifulSoup

def get_soup(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}

    # 构造Request请求 返回<urllib.request.Request object at 0x02C4C450>
    req = urllib.request.Request(url, headers = header)

    # 调用Request.add_header() 添加/修改一个特定的header
    req.add_header("Connection", "keep-alive")

    # 向服务器发送请求 返回<http.client.HTTPResponse object at 0x09135850>
    res = urllib.request.urlopen(req)

    html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup)

    return soup
```