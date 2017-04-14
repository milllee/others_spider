#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: other_test.py
# Create Time: 2017年04月13日 星期四 11时14分17秒
# Author: Miller Lee
# Email: 252343465@qq.com
# ##############################################

name=str(input('你的名字：'))
age=int(input('你的年龄：'))
answer=int(2**10)
exam=0
if age<=12:
    print('儿童玩家，禁止玩各种游戏')
    exit()
elif 12 < age < 17:
    print('限制玩家，请遵守游戏规则')
    exit()
else:
    while exam / answer != 1:
        exam = int(input("你的验证："))
    if exam != answer:
        print("回答错误")
    else:
        print('欢迎{}来到桃花缘，你的年龄是{}岁，在桃花缘里面各种人生际遇，各种玩法需要玩家冒险'.format(name, age))
