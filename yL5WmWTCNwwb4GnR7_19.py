
def return_unique(lst):
  ans =[]
  for i in lst:
    if lst.count(i)== 1:
      ans.append(i)
  return ans

