
def wiggle_string(s):
  a = []
  p = 0
  while p < len(s):
    x = " "*p + s
    a.append(x)
    p += 1
  while p >= 0:
    x = " "*p + s
    a.append(x)
    p -= 1
  
  return a

