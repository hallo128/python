#sp.py

import urllib2
import string
import re
from bs4 import BeautifulSoup

url = 'http://item.jd.com/2385681.html'
myPage = urllib2.urlopen(url).read().decode('gbk')

ll=myPage.encode("gbk")       #ת��Ϊ�ַ���ʽ
soup = BeautifulSoup(ll)

soup1=soup.find_all('table')[2]


def has_class_but_no_id(tag):
    return tag.has_attr('class')

list1=soup1.find_all(has_class_but_no_id)
list11=str(list1[1]).decode('utf-8')
list2=list11.rsplit('</td>')[0].rsplit('>')[1]


list12=str(list1[2]).decode('utf-8')
list3=list12.rsplit('</td>')[0].rsplit('>')[1]

list99=soup1.find_all("tr")                    #�������ת���б�
s=str(list99[2]).decode('utf-8')               #ת��Ϊ�ַ���
list1=s.rsplit('</td>')[0].rsplit('>')[2]      #����
list2=s.rsplit('</td>')[1].rsplit('>')[1]      #ֵ

ml={list1:list2}    #������ֵ
v=[u'Ʒ��',u'�ͺ�']

ml[f]


e={'1':2}
ml.update(e)       #���ֵ�e�ļ�-ֵ��ӵ��ֵ�ml



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
#��ȡ�ű��ļ��ĵ�ǰ·��
def cur_file_dir():
    #��ȡ�ű�·��
    path = sys.path[0]
    #�ж�Ϊ�ű��ļ�����py2exe�������ļ�������ǽű��ļ����򷵻ص��ǽű���Ŀ¼�������py2exe�������ļ����򷵻ص��Ǳ������ļ�·��
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
#��ӡ���
print cur_file_dir()

string=''
for i in range(len(l_k)):
    string=string+'         '+l_k[i]


###############�����ļ�
import codecs
f = codecs.open("out.txt", "w+",'gbk')
f.write(string)
f.close()



a=u'����'
b=a.encode('utf')
f=open(file,"w")
f.write(b)
f.close()
print "successful"     

v=[u'Ʒ��',u'�ͺ�']
keep=[]                              #������Ҫ�����
for i in range(len(l_k)):    
    if l_k[i] in v:
        keep.append(i)
        #keep.append(l_k.index(v[1]))        

l_k1=[]    #��Ҫ�������
l_v1=[]    #��Ҫ���ֵ                  
for i in range(len(keep)):
    l_k1.append(l_k[keep[i]])
    l_v1.append(l_v[keep[i]])  


url1 = 'http://item.jd.com/2385681.html'
url2 = 'http://item.jd.com/1859122.html'
url=[url1,url2]


import codecs
f = codecs.open("out.txt", "a",'gbk')   #Ҫ����gbk
for i in range(len(url)):
    data(url[i])    
    f.write(text+'\n')
f.close()

    

###############�����ļ�
import codecs
f = codecs.open("out.txt", "w+",'gbk')   #Ҫ����gbk
f.write(string+'\n')
f.close()

f = codecs.open("out.txt", "a",'gbk')   #Ҫ����gbk
f.write(text)
f.close()





