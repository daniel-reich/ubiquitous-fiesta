
def divide(lst, n):
  ret = []
  fill = []
  total = 0
  for x in lst:
    if(total + x > n):
      ret.append(list(fill))
      fill.clear()
      total = 0
    fill.append(x)
    total += x
  ret.append(list(fill))
  return ret

