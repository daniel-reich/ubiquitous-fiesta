
def is_ascending(s):
  if isinstance(s,str):
    for i in range(1,len(s)):
      if len(s) % i == 0:
        lst = list(map(lambda x: int(s[x:x+i]),range(0,len(s),i)))
        if is_ascending(lst):
          return True
    return False
  
  try:
    if s[0] + 1 != s[1]:
      return False
    return is_ascending(s[1::])
  except IndexError:
    return True

