#BugBaidu.py

# -*- coding: utf-8 -*-  
#---------------------------------------  
#   ���򣺰ٶ���������  
#   �汾��0.5  
#   ���ߣ�why  
#   ���ڣ�2013-05-16  
#   ���ԣ�Python 2.7  
#   ������������ַ���Զ�ֻ��¥�������浽�����ļ�  
#   ���ܣ���¥�����������ݴ��txt�洢�����ء�  
#---------------------------------------  
   
import string  
import urllib2  
import re  
  
#----------- ����ҳ���ϵĸ��ֱ�ǩ -----------  
class HTML_Tool:  
    # �÷� ̰��ģʽ ƥ�� \t ���� \n ���� �ո� ���� ������ ���� ͼƬ  
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")  
      
    # �÷� ̰��ģʽ ƥ�� ����<>��ǩ  
    EndCharToNoneRex = re.compile("<.*?>")  
  
    # �÷� ̰��ģʽ ƥ�� ����<p>��ǩ  
    BgnPartRex = re.compile("<p.*?>")  
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")  
    CharToNextTabRex = re.compile("<td>")  
  
    # ��һЩhtml�ķ���ʵ��ת��Ϊԭʼ����  
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]  
      
    def Replace_Char(self,x):  
        x = self.BgnCharToNoneRex.sub("",x)  
        x = self.BgnPartRex.sub("\n    ",x)  
        x = self.CharToNewLineRex.sub("\n",x)  
        x = self.CharToNextTabRex.sub("\t",x)  
        x = self.EndCharToNoneRex.sub("",x)  
  
        for t in self.replaceTab:    
            x = x.replace(t[0],t[1])    
        return x    
      
class Baidu_Spider:  
    # ������ص�����  
    def __init__(self,url):    
        self.myUrl = url + '?see_lz=1'  
        self.datas = []  
        self.myTool = HTML_Tool()  
        print u'�Ѿ������ٶ��������棬��������'  
    
    # ��ʼ������ҳ�沢����ת�봢��  
    def baidu_tieba(self):  
        # ��ȡҳ���ԭʼ��Ϣ�������gbkת��  
        myPage = urllib2.urlopen(self.myUrl).read().decode("utf-8")  
        # ����¥����������һ���ж���ҳ  
        endPage = self.page_counter(myPage)  
        # ��ȡ�����ı���  
        title = self.find_title(myPage)  
        print u'�������ƣ�' + title  
        # ��ȡ���յ�����  
        self.save_data(self.myUrl,title,endPage)  
  
    #��������һ���ж���ҳ  
    def page_counter(self,myPage):  
        # ƥ�� "����<span class="red">12</span>ҳ" ����ȡһ���ж���ҳ  
        myMatch = re.search(r'class="red">(\d+?)</span>', myPage, re.S)  
        if myMatch:    
            endPage = int(myMatch.group(1))  
            print u'���汨�棺����¥������%dҳ��ԭ������' % endPage  
        else:  
            endPage = 0  
            print u'���汨�棺�޷�����¥�����������ж���ҳ��'  
        return endPage  
  
    # ����Ѱ�Ҹ����ı���  
    def find_title(self,myPage):  
        # ƥ�� <h1 class="core_title_txt" title="">xxxxxxxxxx</h1> �ҳ�����  
        myMatch = re.search(r'<h1.*?>(.*?)</h1>', myPage, re.S)  
        title = u'���ޱ���'  
        if myMatch:  
            title  = myMatch.group(1)  
        else:  
            print u'���汨�棺�޷��������±��⣡'  
        # �ļ������ܰ��������ַ��� \ / �� * ? " < > |  
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')  
        return title  
  
  
    # �����洢¥������������  
    def save_data(self,url,title,endPage):  
        # ����ҳ�����ݵ�������  
        self.get_data(url,endPage)  
        # �򿪱����ļ�  
        f = open(title+'.txt','w+')  
        f.writelines(self.datas)  
        f.close()  
        print u'���汨�棺�ļ������ص����ز������txt�ļ�'  
        print u'�밴������˳�...'  
        raw_input();  
  
    # ��ȡҳ��Դ�벢����洢��������  
    def get_data(self,url,endPage):  
        url = url + '&pn='  
        for i in range(1,endPage+1):  
            print u'���汨�棺����%d�����ڼ�����...' % i  
            myPage = urllib2.urlopen(url + str(i)).read()  
            # ��myPage�е�html���봦���洢��datas����  
            self.deal_data(myPage.decode('gbk'))  
              
  
    # �����ݴ�ҳ������пٳ���  
    def deal_data(self,myPage):  
        myItems = re.findall('id="post_content.*?>(.*?)</div>',myPage,re.S)  
        for item in myItems:  
            data = self.myTool.Replace_Char(item.replace("\n","").encode('utf-8'))  
            self.datas.append(data+'\n')  
  
  
