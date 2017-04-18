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
   
                 

a = '<html><div class="njfen">98</div><div class="test">100</div></html>'


my = MyHtmlPaser()
my.feed(a)
print my.scope
