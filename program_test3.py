#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: program_test3.py
# Create Time: 2017年04月13日 星期四 18时28分12秒
# Author: Miller Lee
# Email: 252343465@qq.com
# ##############################################

import urllib2
import re

def savetofile(num,count):
    file_object = open('thefile.txt', 'a+')
    line = str(num) + ' ' + count[0] + '\n'
    file_object.write(line)
    file_object.close( )
    
def geturl(url,num):
    searchurl = url + str(num)
    print(searchurl),
    data=urllib2.urlopen(searchurl)
    html = data.read() 
    data.close()
    print(html)
    rebaidu = re.compile(r'百度为您找到相关结果约(.*?)个')
    allbaidu = re.findall(rebaidu,html)
    print(allbaidu)
    savetofile(num,allbaidu)
if __name__=='__main__':
    for x in xrange(100):
        geturl('http://www.baidu.com/s?wd=',x)
