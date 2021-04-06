
def n_differences(lst):
  while len(lst) > 1:
    lst = descrease(lst)
  return lst[0]
​
def descrease(lst):
  return [lst[i + 1] - lst[i] for i in range(0,len(lst) - 1, 1)]

