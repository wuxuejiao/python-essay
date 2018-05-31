#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

class xiaoshuo(object):
    def __init__(self):
        self.names = []
        self.urls = []
        self.texts = ''
        self.url = 'http://www.biqukan.com/1_1094/'
    def download_url(self):
        req = requests.get(self.url)
        html= req.text
        div= BeautifulSoup(html)
        div_list=div.find_all('div',class_ = 'listmain')
        a = BeautifulSoup(str(div_list))
        a_list = a.find_all('a')
        for each in a_list[15:]:
            self.urls.append('http://www.biqukan.com'+each.get('href'))
            self.names.append(each.string)
    def get_content(self,target):
        req = requests.get(target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div',class_ = 'showtxt')
        texts = str(texts).replace('<br/><br/>','\n')
        texts = texts.split('id="content">')[1]
        return texts

if __name__ == "__main__":
    dl = xiaoshuo()
    dl.download_url()
    n = len(dl.names)
    print n
    fo = open("a.txt","a")
    for i in range (n) :
       # fo.write(dl.names[i]+'\n')
        fo.write(dl.get_content(dl.urls[i]))
        fo.write('\n\n')
    print 'download finish'
    fo.close()



