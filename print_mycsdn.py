#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

class my_csdn(object):
    def print_csdn(self,url):
        s = requests.Session()
        r = s.get(url)
        html = BeautifulSoup(r.text)
        div = html.find_all('h4')
        div_t= BeautifulSoup(str(div))
        div_title1 = div_t.find_all('a')
        # 获取文章题目
        div_title = []
        for each in div_title1:
            div_title.append(str(each).split('</span>')[1].split('</a>')[0])
        # 获取阅读数、评论数
        read_num = html.find_all('span',class_ = 'read-num')
        l1 = len(div_title)
        j=0
        i=0
        while i < l1 :
            print div_title[i],read_num[j].string,read_num[j+1].string
            i+=1
            j+=2
    
if __name__ == "__main__":
    url = 'https://blog.csdn.net/weixin_40748006/article/list/1'
    c = my_csdn()
    c.print_csdn(url)
    
    
