#!/usr/bin/python
# coding: utf-8
# Author:      illuz <iilluzen[at]gmail.com>
# File:        jj.py
# Create Date: 2015-03-18 19:19:07
# Usage:       jj.py 来自风平浪静的明天 2
# Descripton:  从 bilibili 搜索新番，再到 bilibilijj 得到 MP3/MP4/ASS 地址。

import sys
from pyquery import PyQuery as pq
import time

def get_vedio_sub(url, fp):
    jj_url = url.replace('bilibili', 'bilibilijj')
    # print('Getting' + jj_url)
    jj_page = pq(jj_url)
    fp.write('#### ' + jj_page('title').text().encode('utf-8') + '\n')
    for elem in jj_page('.Data_Data > a'):
        link = jj_page(elem).attr('href').encode('utf-8')
        if '.mp3' in link:
            link = 'http://www.bilibilijj.com' + link
            print link
            fp.write('- [MP3](' + link + ')\n')
        elif '.mp4' in link:
            link = 'http://www.bilibilijj.com' + link
            print link
            fp.write('- [MP4](' + link + ')\n')
        elif 'ass' in link:
            print link
            fp.write('- [ASS](' + link + ')\n')
    fp.write('\n---\n\n')


def get_jj_urls(name, num):
    fp = open('res.md', 'w')
    url = 'http://www.bilibili.com/search_v2?keyword=' + name + '&orderby=&type=video&tids=33&page='
    for i in range(1, num + 1):
        page = pq(url + str(i))
        # print page
        for elem in page('.r_sp > a'):
            get_vedio_sub(page(elem).attr('href'), fp)


def main():
    # get_jj_urls('来自风平浪静的明天', 1)
    if len(sys.argv) != 3:
        print("2 parameter!")
        return
    else:
        get_jj_urls(sys.argv[1], int(sys.argv[2]))


if __name__ == '__main__':
    main()



