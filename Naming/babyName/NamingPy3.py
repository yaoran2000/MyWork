#encoding:utf-8

import urllib, urllib2


#输出结果文件
resultFile = open('/app/naming/yangxu.txt','w+')
                  
i = 0

#0x9fa6  0x4eff

for ch in xrange(0x4e00,0x9fa6):
  data = {}
  data['word1'] = '杨'
  data['word2'] =  '旭' + unichr(ch).encode('gbk')
  data['st'] = '2'
  data['FrontType'] = '1'
  data['Submit'] = '开始测算'

  babyname = '\n杨' + '旭' + unichr(ch).encode('gbk')+','
  url_values = urllib.urlencode(data)

  url = 'http://www.1518.com/s'
  full_url = url + '?' + url_values
  f = urllib2.urlopen(full_url)

  #解析html文本
  #print f.read()
  html_str = f.read()
  score_str = '<div class="name_num">'
  p = html_str.find(score_str)
  if not p == -1:
      score = html_str[p+22:p+24].replace('<','').replace('>','')
      #输出到文件
      resultFile.write(babyname)
      resultFile.write(score)
      i = i + 1
      print '\n %s', i
      print babyname + score

resultFile.close();