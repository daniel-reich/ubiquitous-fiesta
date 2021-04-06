
def valid_rondo(s):
  if len(s) == 1:
    return False
  if not s[0] == s[-1] == 'A':
    return False
    
  last = -1
  for c in "BCDEFGHIJ":
    try :
      if s.index(c) < last:
        return False
      last = s.index(c)
    except : pass
    
  for i in range(0,len(s)-1):
    if s[i] == s[i+1]:
      return False
  return True

