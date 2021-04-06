
def decP(n):
  for i,c in enumerate(str(n)[::-1]):
    if c == '.':
      return i
  return 0
​
def drange(*args):
  if len(args) == 1:
    a, b, c = 0, args[0], 1
  elif len(args) == 3:
    a,b,c = args
  else:
    a,b = args
    c = 1
  
  maxP = max(decP(n) for n in [a,b,c])
  
  lst = []
  while a < b:
    lst.append(round(a,maxP))
    a += c
  return tuple(lst)

