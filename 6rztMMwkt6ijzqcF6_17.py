
def is_repeated(strn):
  x = [24,12,8,6,4,3,2]
  for k in x:
    for i in range(int(24/k), 24):
      a = i
      while (a - (24/k)) >= 0:
        a = a - (24/k)
      if strn[int(a)] != strn[i]:
        break
      elif i == 23:
        return int(k)
  return False

