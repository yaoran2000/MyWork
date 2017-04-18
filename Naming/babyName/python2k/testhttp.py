# -*- coding: cp936 -*-
#http://www.1518.com/s?st=2&word1=%D2%A6&word2=%C7%E5%D4%B4&Submit=%BF%AA%CA%BC%B2%E2%CB%E3
import urllib, urllib2

resultFile = open('c:/temp/result.html','w+')
                  

data = {}
data['word1'] = '姚'
data['word2'] = '清源'
data['st'] = '2'
data['Submit'] = '开始测算'

url_values = urllib.urlencode(data)
url = 'http://www.1518.com/s'
full_url = url + '?' + url_values
f = urllib2.urlopen(full_url)
resultFile.write(f.read())

resultFile.close();
