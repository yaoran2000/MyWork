# -*- coding: gbk -*-
import urllib, urllib2
from HTMLParser import HTMLParser


class MyHtmlPaser(HTMLParser):
    is_scope=0
    scope=0
    def __init__(self):
        HTMLParser.__init__(self)
        self.scope = 0
        self.is_scope=0
        
    def handle_starttag(self,tag,attrs):
        self.is_scope=0
        if tag == "div":
            for name,value in attrs:
              if name == "class":
                 if value == "njfen":
                    self.is_scope=1
           
        
    def handle_data(self,text):
        if self.is_scope:            
           self.scope=text    



#�������ļ�
resultFile = open('c:/temp/1.txt','w+')
                  



#for ch in xrange(0x4e00,0x9fa6):
data = {}
data['word1'] = 'Ҧ'
data['word2'] = '��Դ' #unichr(ch).encode('gbk')
data['st'] = '2'
data['Submit'] = '��ʼ����'

babyname = '\nҦ��Դ,' #+ unichr(ch)
url_values = urllib.urlencode(data)

url = 'http://www.1518.com/s'
full_url = url + '?' + url_values
f = urllib2.urlopen(full_url)

#����html�ı�
my = MyHtmlPaser()
my.feed(f.read().decode('gbk'))

#������ļ�
resultFile.write(babyname)
resultFile.write(my.scope)


resultFile.close();


