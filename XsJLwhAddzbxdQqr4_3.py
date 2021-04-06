
def difference_max_min(lst):
  mx=lst[0]
  mi=lst[0]
  for i in lst:
    if mx<i:
      mx=i
    if mi>i:
      mi=i
  return mx-mi

