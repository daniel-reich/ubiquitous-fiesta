
def is_repeated(strn):  
  temp = (strn + strn).find(strn, 1, -1) 
  res = len(strn) / temp
  if res < 0:
    return False
  else : return res

