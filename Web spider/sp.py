#sp.py

import urllib2
import string
import re
from bs4 import BeautifulSoup

url = 'http://item.jd.com/2385681.html'
myPage = urllib2.urlopen(url).read().decode('gbk')

ll=myPage.encode("gbk")       #转换为字符格式
soup = BeautifulSoup(ll)

soup1=soup.find_all('table')[2]


def has_class_but_no_id(tag):
    return tag.has_attr('class')

list1=soup1.find_all(has_class_but_no_id)
list11=str(list1[1]).decode('utf-8')
list2=list11.rsplit('</td>')[0].rsplit('>')[1]


list12=str(list1[2]).decode('utf-8')
list3=list12.rsplit('</td>')[0].rsplit('>')[1]

list99=soup1.find_all("tr")                    #将表格按行转成列表
s=str(list99[2]).decode('utf-8')               #转换为字符型
list1=s.rsplit('</td>')[0].rsplit('>')[2]      #属性
list2=s.rsplit('</td>')[1].rsplit('>')[1]      #值

ml={list1:list2}    #属性与值
v=[u'品牌',u'型号']

ml[f]


e={'1':2}
ml.update(e)       #将字典e的键-值添加到字典ml



for i in range(len(l_k)):
    print l_k[i]

for i in range(len(l_v)):
    print l_v[i]



g=[]
for i in range(len(list99)):    
    if '<' in l_k[i]:
        #l_k1.pop(i)
        g.append(i)
        #print l_k1[i]
        
g.reverse()
for i in range(len(g)):
    l_k.pop(g[i])
    l_v.pop(g[i])

#---------
import sys,os
#获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
#打印结果
print cur_file_dir()

string=''
for i in range(len(l_k)):
    string=string+'         '+l_k[i]


###############读出文件
import codecs
f = codecs.open("out.txt", "w+",'gbk')
f.write(string)
f.close()



a=u'中文'
b=a.encode('utf')
f=open(file,"w")
f.write(b)
f.close()
print "successful"     

v=[u'品牌',u'型号']
keep=[]                              #不符合要求的行
for i in range(len(l_k)):    
    if l_k[i] in v:
        keep.append(i)
        #keep.append(l_k.index(v[1]))        

l_k1=[]    #按要求的属性
l_v1=[]    #按要求的值                  
for i in range(len(keep)):
    l_k1.append(l_k[keep[i]])
    l_v1.append(l_v[keep[i]])  


url1 = 'http://item.jd.com/2385681.html'
url2 = 'http://item.jd.com/1859122.html'
url=[url1,url2]


import codecs
f = codecs.open("out.txt", "a",'gbk')   #要求是gbk
for i in range(len(url)):
    data(url[i])    
    f.write(text+'\n')
f.close()

    

###############读出文件
import codecs
f = codecs.open("out.txt", "w+",'gbk')   #要求是gbk
f.write(string+'\n')
f.close()

f = codecs.open("out.txt", "a",'gbk')   #要求是gbk
f.write(text)
f.close()





