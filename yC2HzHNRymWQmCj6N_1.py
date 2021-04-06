
def less_or_equal(lst, k):
  if len(lst) == k:
    return lst[-1]
​
  for x in range(1,9):
    if sum(1 for n in lst if x >= n) == k:
      return x

