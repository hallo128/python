#jd_home.py
# -*- coding: utf-8 -*-  
import urllib2
import string
import re
from bs4 import BeautifulSoup

#url='http://search.jd.com/Search?keyword=%E9%94%A4%E5%AD%90&enc=utf-8&wq=%E9%94%A4%E5%AD%90&pvid=i7hnzini.4mbbtl'
#url='http://search.jd.com/Search?keyword=oppo&enc=utf-8&wq=oppo&pvid=fj2ackni.4mbbtl'
#url='http://search.jd.com/Search?keyword=LG&enc=utf-8&wq=LG&pvid=xeecekni.4mbbtl'
#url='http://search.jd.com/Search?keyword=%E9%AD%85%E6%97%8F&enc=utf-8&wq=%E9%AD%85%E6%97%8F&pvid=drht4lni.4mbbtl'
#url='http://search.jd.com/Search?keyword=vivo&enc=utf-8&wq=vivo&pvid=1f615lni.4mbbtl'
url='http://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M2800L4499&go=0&JL=2_1_0#J_crumbsBar'
myPage = urllib2.urlopen(url).read().decode('utf-8')

ll=myPage.encode("utf-8")       #转换为字符格式
soup = BeautifulSoup(ll)



def has_data_sku(tag):
    return tag.has_attr('data-sku')
sample=soup.find_all(has_data_sku)


s_sample=[]            #转换为字符型
for i in range(len(sample)):
    s_sample.append(str(sample[i]))


s_good=[]              #提出指定商品   <li class="gl-item" data-sku="1220052">
for i in range(len(s_sample)):
    if '<li' in s_sample[i]:
        s_good.append(s_sample[i])
        



 
#------------------商品价格
s_price=[]
rm=[]
for i in range(len(s_good)):
    soup4 = BeautifulSoup(s_good[i])
    good_price=soup4.find("strong")           #找价格
    s_good_price=str(good_price)
    if '</i>' in s_good_price:
        s_price.append(s_good_price.rsplit('</i>')[0].rsplit('<i>')[1]) #提出价格
    else:
        rm.append(i)

#--------------------更新可用商品
for i in range(len(rm)):    
    s_good.pop(rm[i])


#------------------商品编号id   s_good[0].split('\">')[0].rsplit('\"')[3]
good_id=[]          
for i in range(len(s_good)):
    idl=s_good[i].split('\">')[0].rsplit('\"')[3]
    good_id.append(idl)

'''
s_price=[]
for i in range(len(s_good)):
    soup4 = BeautifulSoup(s_good[i])
    good_price=soup4.find("strong")           #找价格
    s_good_price=str(good_price)
    s_price.append(s_good_price.rsplit('</i>')[0].rsplit('<i>')[1]) #提出价格
'''

#------------------商品评价数
s_judge=[]
for i in range(len(s_good)):
    soup4 = BeautifulSoup(s_good[i])
    good_judge=soup4.find_all("strong")[1]
    s_good_judge=str(good_judge)
    s_judge.append(s_good_judge.rsplit('</a>')[0].rsplit('>')[2])

    
soup4 = BeautifulSoup(s_good[0])
target="_blank"
good_judge=soup4.find_all("strong")[1]
s_good_judge=str(good_judge)
s_good_judge.rsplit('</a>')[0].rsplit('>')[2]
#----------------------------------------------------------------

import urllib2
import string
import re
from bs4 import BeautifulSoup


def data(url):

    myPage = urllib2.urlopen(url).read().decode('gbk')

    ll=myPage.encode("gbk")       #转换为字符格式
    soup = BeautifulSoup(ll)

    #------------------指标：商品编号
    soup_id=soup.find('div','fl')
    s_id=str(soup_id).decode('utf-8')
    id_k=s_id.rsplit('</')[0].rsplit('>')[2]
    id_v=s_id.rsplit('</')[1].rsplit('>')[2]

    #----------------------------基本属性
    tb=soup.find_all('table')
    soup1=tb[len(tb)-1]       #table[2]
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

    #----------------------------整理所有属性
    l_k1.insert(0,id_k)
    l_v1.insert(0,id_v)
    l_k=l_k1
    l_v=l_v1


    #---------------对字符进行处理(去除字符串后的括号)
    for i in range(len(l_v)): 
        if '(' in l_v[i]:
            l_v[i]=l_v[i].split('(')[0]

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





#该页的全部网址
jdurl=[]
for i in range(len(good_id)):
    jdurl.append('http://item.jd.com/' + good_id[i]+'.html') 


import codecs
data(jdurl[0])
#---------------添加价格、评价数
string=string+','+u'价格'+','+u'评价数'

f = codecs.open("out.txt", "w+",'gbk')   #要求是gbk
f.write(string+'\n')
f.close()



f = codecs.open("out.txt", "a",'gbk')   #要求是gbk
for i in range(len(jdurl)):
    data(jdurl[i])
    #---------------添加价格、评价数
    text=text+','+s_price[i]+','+s_judge[i]

    f.write(text+'\n')
f.close()




