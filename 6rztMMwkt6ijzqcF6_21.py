
def is_repeated(s):
  res=None
  temp = (s + s).find(s, 1, -1) 
  if temp!=-1:
    res = s[:temp]
  else:
    return False
  return s.count(res)

