#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: program_test1.py
# Create Time: 2017年04月13日 星期四 17时55分58秒
# Author: Miller Lee
# Email: 252343465@qq.com
# ##############################################

phone_book = {}
for i in range(3):
    name = input('请输入姓名:')
    phone = input('请输入电话号码:')
    phone_book[name] = phone

print('电话记录已保存！')
check_name = input('请输入要查询的人:')
if check_name in phone_book.keys():
    print('此人的电话是:{}'.format(phone_book[check_name]))
else:
    print('查无此人！')
