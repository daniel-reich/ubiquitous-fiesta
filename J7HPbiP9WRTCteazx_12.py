
def n_differences(lst):
  res = []
  
  while len(lst) != 1:
    for i in range(len(lst)-1):
      res.append(lst[i+1] - lst[i])
​
    lst = res
    res = []
  
  return lst[0]

