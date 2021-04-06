
def simple_pair(lst, n):
​
  for i in lst:
​
    if i == 0:
      continue
​
    j = n / i
    if i == j and lst.count(i) > 1:
      return [i, j]
    elif i != j and j in lst:
      return [i, j]
​
  return None

