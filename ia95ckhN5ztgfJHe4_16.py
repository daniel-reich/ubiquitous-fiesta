
def comments_correct(txt):
  txt=txt.replace('/**/','')
  txt=txt.replace('//','')
  return not len(txt)>0

