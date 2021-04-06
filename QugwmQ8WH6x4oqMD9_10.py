
def count_identical_lists(lst1, lst2, lst3, lst4):
  a=[lst1, lst2, lst3, lst4]
  ans=len(a)-len(set(tuple(i) for i in a))
  if ans==0: return ans
  return ans+1

