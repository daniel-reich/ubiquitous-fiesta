
def get_subsets(lst, n):
  x = len(lst)
  temp = []
  for i in range(1 << x):
    temp.append([lst[j] for j in range(x) if (i & (1 << j))])
​
  a = 0
  while a < len(temp):
    if len(temp[a]) == 0:
      del temp[a]
    elif sum(temp[a]) != n:
      del temp[a]
    else:
      a += 1
  temp = sorted(temp)
  temp = sorted(temp, key = len)
  return temp

