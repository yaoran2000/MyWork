# -*- coding: cp936 -*-
namefile = open('c:/temp/namelist.txt','w+')

for ch in xrange(0x4e00,0x9fa6):
    #print u'Ҧ' + unichr(ch)
    namestr = u'\nҦ' + unichr(ch)
    namefile.write(namestr.encode("gbk"))

namefile.close()
