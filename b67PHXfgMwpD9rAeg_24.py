
def plus_sign(txt):
  s=['1','2','3','4','5','6','7','8','9','0','+']
  for i in range(0,len(txt),2): 
    if(txt[i] not in s):
      return False
  return True

