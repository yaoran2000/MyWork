from urllib import parse, request




#输出结果文件
resultFile = open('/app/naming/yangxu.txt','wb')
                  
i = 0

#0x9fa6  0x4eff

for ch in range(0x4e00,0x9fa6):
  data = {}
  data['word1'] = '杨'
  data['word2'] =  '旭' + chr(ch)
  data['st'] = '2'
  data['FrontType'] = '1'
  data['Submit'] = '开始测算'

  babyname = '\n杨' + '旭' + chr(ch)+','
  babynamel = babyname.encode('utf-8')

  url_values = parse.urlencode(data)

  url = 'http://www.1518.com/s'
  full_url = url + '?' + url_values
  resource = request.urlopen(full_url)

  #解析html文本
  #print f.read()
  html_str = resource.read() #.decode('utf-8',errors="ignore")
  #html_str = requests.get(full_url).text
  #encoding = extract(str(html_bytes).lower(), 'charset=', '"')
  #html_str = html_bytes.decode('gb2312')
  #html_str = html_bytes.decode("utf8")

  score_str = b'<div class="name_num">'
  p = html_str.find(score_str)
  if not p == -1:
      score_bytes = html_str[p+22:p+24]
      score = str(score_bytes).replace('<','').replace('>','')
      #输出到文件
      resultFile.write(babynamel)
      resultFile.write(score.encode('utf-8'))
      i = i + 1
      print('\n %s', i)
      print('%s %s', babynamel,score.encode('utf-8'))

resultFile.close();