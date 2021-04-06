
def cap_to_front(s):
  uppers = [l for l in s if l.isupper()]
  lowers = [l for l in s if l.islower()]
  res = uppers + lowers 
  return ''.join(res)

