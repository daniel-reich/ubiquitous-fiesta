
def wrap(s, w):
    return [s[i:i + w] for i in range(0, len(s), w)]
​
​
def ascending(txt):
  st = 1
  i=0
  for j in range(len(txt)):
    X = wrap(txt, j+1)
    fo =0
    for i in range(len(X)-1):
      if int(X[i+1]) == int(X[i]) +1:
        fo = 1
      else:
        fo =0
        break
    if fo:
      return True
  return False

