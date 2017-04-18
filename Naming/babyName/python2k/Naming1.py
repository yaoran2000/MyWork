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



#输出结果文件
resultFile = open('c:/temp/1.txt','w+')
                  



#for ch in xrange(0x4e00,0x9fa6):
data = {}
data['word1'] = '姚'
data['word2'] = '清源' #unichr(ch).encode('gbk')
data['st'] = '2'
data['Submit'] = '开始测算'

babyname = '\n姚清源,' #+ unichr(ch)
url_values = urllib.urlencode(data)

url = 'http://www.1518.com/s'
full_url = url + '?' + url_values
f = urllib2.urlopen(full_url)

#解析html文本
my = MyHtmlPaser()
my.feed(f.read().decode('gbk'))

#输出到文件
resultFile.write(babyname)
resultFile.write(my.scope)


resultFile.close();


