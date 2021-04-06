
def nearest_element(n, lst):
  count=0
  values_min=[]
  values_diff=[]
  for i in lst:
    values_min.append(abs(n-i))
  for i in values_min:
    if i==min(values_min):
      values_diff.append(lst[count])
    count+=1
  return(lst.index(max(values_diff)))

