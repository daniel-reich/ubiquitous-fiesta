
def plus_sign(txt):
  s = len([x for x in txt if x.isalpha()])
  d =  sum(1 for x in range(1,len(txt)) if txt[x].isalpha() and txt[x-1] =='+')
  return d == s

