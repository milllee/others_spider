#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: other_test_1.py
# Create Time: 2017年04月13日 星期四 14时11分56秒
# Author: Miller Lee
# Email: 252343465@qq.com
# ##############################################

name = input('请输入你的姓名:')
s1, s2 = '', ''
try:
    while not (s1 in range(0, 101) and s2 in range(0, 101)):
        s1 = int(input('请输入第一学期成绩:'))
        s2 = int(input('请输入第二学期成绩:'))
        if s1 == 0:
            raise ZeroDivisionError # 抛出被除数等于0的异常
except ZeroDivisionError: # 捕获上面抛出的异常，只显示自定义信息
    print('第一学期成绩为0，不能计算')
except ValueError: # 捕获不正确类型的异常
    print('请输入正整数分数!')
else: # 未产生异常才会执行的操作
    r = (s2 - s1) / s1 * 100
    print('{}第二学期的成绩提高了{:.2f}%'.format(name, r))
