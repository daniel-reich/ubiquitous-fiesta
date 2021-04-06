
def is_consecutive(s,ascending = None):
  if isinstance(s,str):
    for i in range(1,len(s)):
      if len(s) % i == 0:
        lst = list(map(lambda x: int(s[x:x+i]),range(0,len(s),i)))
        if is_consecutive(lst,True) or is_consecutive(lst,False):
          return True
    return False
  
  if ascending == True:
    try:
      if s[0] + 1 != s[1]:
        return False
      return is_consecutive(s[1::],True)
    except IndexError:
      return True
  else:
    try:
      if s[0] - 1 != s[1]:
        return False
      return is_consecutive(s[1::],False)
    except IndexError:
      return True

