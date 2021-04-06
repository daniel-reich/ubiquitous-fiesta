
def possible_palindrome(txt):
  l = len(txt)
  if l == 2 and txt[0] != txt[1]:
    return False
  cdict = {}
  for i in txt:
      cdict[i] = cdict.get(i,0)+1
  
  if l % 2 == 0:
    c = 0
    for i in cdict.values():
      if i%2 == 0:
        c+=1
    if c == len(cdict):
      return True
    else:
      return False
  else:
    d = 0
    for i in cdict.values():
      if i%2 != 0:
        d+=1
    if d!= 1:
      return False
  return True

