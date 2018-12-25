#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wukong'
__date__ = '2018/12/1 10:29'

import time
import pdfkit
from urllib import request, parse
from bs4 import BeautifulSoup

# 配置path后 可以不写
path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # wkhtmltopdf安装位置
config = pdfkit.configuration(wkhtmltopdf=path_wk)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body align=certer>
{body}
</body>
</html>

"""

baseUrl = "https://www.yixi.tv/speech/"


def get_html(index):

    htmlUrl = baseUrl+index
    # <urllib.request.Request object at 0x02C4C450>
    req = request.Request(htmlUrl)
    # <http.client.HTTPResponse object at 0x09135850>
    res = request.urlopen(req)
    html = res.read().decode()
    # 得到BeautifulSoup对象 并按标准格式输出
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find(class_='speech-qa')
    author_tag = soup.find(class_="userInfoWrap")
    article = soup.find(class_="detailContent").p

    # 取出字符串
    try:
        title = '第'+index+'期--'+title_tag.contents[1].string
        title = title.replace(' ', '')
        title = title.replace('"', '')
        title = title.replace('#', '')
        date = title_tag.contents[3].string
        tips = title_tag.contents[5].string
        author = '作者：'+author_tag.contents[7].string + \
            "  "+author_tag.contents[11].string

        articles = ""
        for i in article.contents:
            articles += str(i)
    except BaseException as i:
        title = date = tips = author = articles = "错误"

    titles = "<b style='font-size:30px;'>" + title+"</b>"+"<br>"
    author_date = "<dd style='font-size:20px;'> <i > " + \
        author+"    "+date+"</i></dd>"+"<br>"
    # tips = "<p >"+tips+" < /p >"
    articles = "<article style='font-size: 16px'>"+articles + "</article >"

    body = titles+author_date+tips+"<hr >"+articles

    html = html_template .format(body=body)
    return html, title


def save_pdf(html, file_name):
    options = {
        # 'quiet': ''
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': "UTF-8",
        # 'font_size': 20,

        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.from_string(html, file_name, options=options, configuration=config)


def main():

    start = time.time()
    for i in range(697, 726):
        html, title = get_html(str(i))
        file_name = title+".pdf"
        print(file_name)
        save_pdf(html, file_name)

    total_time = time.time() - start

    print("总共耗时：%.2f 秒" % total_time)


if __name__ == '__main__':
    main()
