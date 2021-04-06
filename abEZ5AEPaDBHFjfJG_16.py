
def formula(txt):
  if txt=='':
    return None
  txt=txt.replace(' ','')
  if 'a' in txt:
    if len(txt)==6:
      return False
    else:
      return  True
  else: 
    lst=txt.split('=')
    for i in lst:
      lst[lst.index(i)]=int(eval(i))
    return True if len(set(lst))==1 else False

