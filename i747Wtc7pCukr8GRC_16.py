
def max_product(lst):
  lst.sort()
  if lst[0] * lst[1] * lst[-1]> lst[-1] * lst[-2] * lst[-3]:
    return lst[-1] * lst[0] * lst[1]
  
  return lst[-1] * lst[-2] * lst[-3]
  
​
def min_product(lst):
  lst.sort()
  if lst[-1] * lst[-2] * lst[0] < lst[1] * lst[2] * lst[0]:
    return lst[-1] * lst[-2] * lst[0]
  return lst[1] * lst[2] * lst[0]

