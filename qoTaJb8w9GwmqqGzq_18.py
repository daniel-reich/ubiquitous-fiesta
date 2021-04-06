
def is_subset(lst1, lst2):
  ans=True
  for i in lst1:
    if not i in lst2:
      ans=False
  return ans

