
def swap_xy(s):
  l = [] 
  s = eval('[' + s + ']')
  s = [list(i) for i in s]
  for i in s:
    l.append((i[-1], i[0]))
​
​
  l = str(l).replace('[', "").replace(']', "")
  return l

