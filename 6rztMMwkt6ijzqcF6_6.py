
def is_repeated(strn):
  rep = None
  tmp = (strn + strn).find(strn, 1, -1) 
  if tmp != -1: 
    rep = strn[:tmp] 
    return strn.count(rep)
  return False

