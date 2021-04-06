
key = [329.63, 246.94, 196, 146.83, 110, 82.41]
def tune(lst):
  global key
  res = []
  for i, val in enumerate(lst):
    if val == 0:
      res += [' - ']
      continue
    p = percent(val,key[i])
    if p > 100:
      if p > 102:
        res += ['+<<']
      else:
        res += ['+<']
    elif p < 100:
      if p < 98:
        res += ['>>+']
      else:
        res += ['>+']
    else:
      res += ['OK']
  return res
​
​
def percent(a,b):
  return round((a/b)*100)

