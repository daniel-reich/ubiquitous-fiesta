
def sum_of_slices(lst):
  i, res = 0, []
  for j in range(len(lst)+1):
    if sum(lst[i:j]) > 100:
      res.append(sum(lst[i:j-1]))
      i = j-1
  if i == len(lst)-1: res.append(lst[i])    
  return res

