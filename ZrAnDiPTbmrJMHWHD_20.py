
def is_central(txt):
 if len(txt)%2==0:
  return False
 pos = int((len(txt)+1)/2)
 return txt[pos-1] != ' '

