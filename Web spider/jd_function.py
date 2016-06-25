#jd_function.py
# -*- coding: utf-8 -*-
import urllib2
import string
import re
from bs4 import BeautifulSoup






def data(url):

    myPage = urllib2.urlopen(url).read().decode('gbk')

    ll=myPage.encode("gbk")       #转换为字符格式
    soup = BeautifulSoup(ll)

    soup1=soup.find_all('table')[2]       #table[2]

    list99=soup1.find_all("tr")                    #将表格按行转成列表



    l_k=[]    #属性
    l_v=[]    #值
    for i in range(len(list99)):
        s=str(list99[i]).decode('utf-8')               #转换为字符型
        list1=s.rsplit('</td>')[0].rsplit('>')[2]      #属性
        list2=s.rsplit('</td>')[1].rsplit('>')[1]

        l_k.append(list1)
        l_v.append(list2)

    v=[u'品牌',u'型号',u'上市年份',u'CPU品牌',u'机身内存',u'运行内存',u'屏幕尺寸',u'分辨率',u'后置摄像头',u'前置摄像头',u'电池容量（mAh）',u'机身尺寸（mm）',u'机身重量（g）']
    keep=[]                              #符合要求的行
    for i in range(len(l_k)):    
        if l_k[i] in v:
            keep.append(i)
        #keep.append(l_k.index(v[1]))        

    l_k1=[]    #按要求的属性
    l_v1=[]    #按要求的值                  
    for i in range(len(keep)):
        l_k1.append(l_k[keep[i]])
        l_v1.append(l_v[keep[i]])

    l_k=l_k1
    l_v=l_v1

    ml={}                             #整理后的字典
    for i in range(len(l_k)):
        e={l_k[i]:l_v[i]}
        ml.update(e)

#按行安排格式
    global string
    string=''   #第一行(unicode)
    for i in range(len(l_k)):
        string=string+','+l_k[i]

    global text
    text=''   #内容 
    for i in range(len(l_v)):
        text=text+','+l_v[i]


