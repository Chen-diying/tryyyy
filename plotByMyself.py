# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:08:20 2019

@author: Tony 陈荻莹
"""
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.rcParams['font.family']='SimHei'  # 更改默认设置，可以显示中文，其中‘SimHei’是黑体字
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('C:\\Users\\Tony\\Desktop\\PYExamples\\test\\liao.xlsx')  # 读取xlsx文件

scores = df['月销量']
score1 = []  # 存储<50的月销量
score2 = []  # 存储200-500的月销量
score3 = []  # 存储>=500的月销量
score4 = []  # 存储50-200的月销量

i = 0
while i < 450:  # 获得<50的月销量并存储进score1
    if(scores[i] < 50):
        score1.append(scores[i])
    i = i+ 1
j = 0
while j < 450:  # 获得200-500的月销量并存储进score2
    if(scores[j] >= 200):
        if(scores[j] < 500):
            score2.append(scores[j])
    j = j+ 1
k = 0
while k < 450:  # 获得>=500的月销量存储进score3
    if(scores[k] >= 500):
        score3.append(scores[k])
    k = k + 1
l = 0
while l < 450:  # 获得50-200的月销量并存储进score4
    if(scores[l] >= 50):
        if(scores[l] < 200):
            score4.append(scores[l])
    l = l + 1

weight4 = len(score4)/450  # 获得50-200的月销量所占比重
weight1 = len(score1)/450  # 获得<50的月销量所占比重
weight2 = len(score2)/450  # 获得200-500的月销量所占比重
weight3 = len(score3)/450  # 获得>=500的月销量所占比重
labels = '< 50销量', '200 - 500销量', '>= 500销量' , '50 - 200销量' # 饼图标签

weight = [weight1, weight2, weight3, weight4]
explode = (0.05, 0.05, 0.05, 0.05)  # 这个是控制分离的距离的，默认的饼图不分离。
plt.title('月销量比重')
plt.pie(weight, labels=labels, explode=explode, startangle=60, autopct='%1.1f%%')  # qutopct在图中显示比例值，注意值的格式。startangle:起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起；
plt.show()

//The file is modified by Geng-long.
