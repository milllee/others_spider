#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: program_test2.py
# Create Time: 2017年04月13日 星期四 18时12分43秒
# Author: Miller Lee
# Email: 252343465@qq.com
# ##############################################

import threading, time

def get_page():
    print('thread {} is running...'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n += 1
        print('threading {} >>> {}'.format(threading.current_thread().name, n))
        time.sleep(0.2)
    print('thread {} is ended.'.format(threading.current_thread().name))


print('thread {} is running...'.format(threading.current_thread().name))
t = threading.Thread(target=get_page, name='LoopThread')
t.start()
t.join()
print('thread {} ended......'.format(threading.current_thread().name))
