a = '<html><div class="njfen">98</div><div class="test">100</div></html>'
b = '<div class="njfen">'
p = a.find(b)
if not p == -1:
   score = a[p+18:p+22]
   c = score.replace('<','').replace('>','')
   print c
