
def widen_streets(lst, n):
  s = []
  v = []
  for i in range(0, len(lst[-1])):
    if lst[-1][i] == ' ':
      s.append(i)
  
  for i in range(0, len(lst)):
    v.append('')
    for j in range(0, len(lst[0])):
      if j in s:
        v[i]+= ' '*n
      else:
        v[i] += lst[i][j]
  return v
​
​
​
  return lst

