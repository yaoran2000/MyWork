# coding=gbk
import urllib, urllib2
#import socket

#socket.setdefaulttimeout(10.0)

#�������ļ�
resultFile = open('/data/named/ci.txt','w+')
                  
i = 0

#0x9fa6  0x4eff

for ch in xrange(0x4e00,0x9fa6):
  data = {}
  data['word'] = '�Ϻ���'+ unichr(ch).encode('gbk') +'�Ƽ����޹�˾'
  data['st'] = '5'
  data['sp'] = '1'
  data['v'] = '1'
  data['submit'] = '1'

  companyname = '\n�Ϻ���'+ unichr(ch).encode('gbk') +'�Ƽ����޹�˾,'
  url_values = urllib.urlencode(data)

  url = 'http://gongsi.1518.com/gongsi.php'
  full_url = url + '?' + url_values

  #time.sleep(0.5)
  try:
    f = urllib2.urlopen(full_url,timeout=3)

    #����html�ı�
    #print f.read()
    html_str = f.read()
    score_str = 'class="con_sub_title">'
    p = html_str.find(score_str)
    if not p == -1:
        score = html_str[p+152:p+158].replace('<','').replace('>','')
        #������ļ�
        resultFile.write(companyname)
        resultFile.write(score)
        i = i + 1
        print '\n %s', i
        print companyname + score
  except Exception,e:
    print 'Error: ' + companyname
    print str(e)
    

resultFile.close();


