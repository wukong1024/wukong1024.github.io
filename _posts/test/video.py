#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wukong'
__date__ = '2018/12/1 10:29'

import time
import sys
from urllib import request, parse
from bs4 import BeautifulSoup


baseUrl = "https://www.yixi.tv/speech/"


class ShowProcess():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    i = 0  # 当前的处理进度
    max_steps = 0  # 总共需要处理的次数
    max_arrow = 50  # 进度条的长度
    infoDone = 'done'

    # 初始化函数，需要知道总共的处理次数
    def __init__(self, max_steps, infoDone='Done'):
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone

    # 显示函数，根据当前的处理进度i显示进度
    # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps)  # 计算显示多少个'>'
        num_line = self.max_arrow - num_arrow  # 计算显示多少个'-'
        percent = self.i * 100.0 / self.max_steps  # 计算完成进度，格式为xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r'  # 带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(process_bar)  # 这两句打印字符到终端
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0


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
    title = ""
    video_url = ""
    try:
        title = '第'+index+'期--'+title_tag.contents[1].string
        title = title.replace(' ', '')
        title = title.replace('"', '')
        title = title.replace('#', '')
        title = title+".mp4"
        video_url = soup.find(type="video/mp4").get("src")

    except BaseException as i:
        print(i)
    return title, video_url


def schedule(a, b, c):

    max_steps = c
    process_bar = ShowProcess(max_steps, '下载完成')
    i = a*b
    process_bar.show_process(i)


def main():
    ss = int(input("起点: ")) or 0
    dd = int(input("终点: ")) or 769
    start = time.time()
    for i in range(ss, dd):
        title, video_url = get_html(str(i))
        print(title, video_url)
        if title and video_url:
            try:
                request.urlretrieve(video_url, title, schedule)
            except BaseException as i:
                print(i)

    total_time = time.time() - start

    print("总共耗时：%.2f 秒" % total_time)


if __name__ == '__main__':
    main()
