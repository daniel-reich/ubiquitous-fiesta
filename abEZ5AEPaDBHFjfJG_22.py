
def formula(txt):
  if not 'a' in txt and txt!='':return eval(txt.replace('=','=='))
  if 'a' in txt:
    txt=txt.split('=');a=1
    while eval(txt[1])!=eval(txt[0]):
      mem=abs(eval(txt[1])-eval(txt[0]));a+=1
      if abs(eval(txt[1])-eval(txt[0]))>mem:break
    return eval(txt[1])==eval(txt[0])

