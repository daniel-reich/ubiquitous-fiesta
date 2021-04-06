
def is_repeated(s):
  temp,x = s[0],s[1:]
  while temp != x[:len(temp)]:
    temp+=x[0]
    x = x[1:]
    if len(temp)*2>len(s)+1: return False
  return s.count(temp)

