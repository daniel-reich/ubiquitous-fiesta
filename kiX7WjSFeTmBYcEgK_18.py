
def major_sum(lst):
  n = sum(i for i in lst if i < 0)
  p = sum(lst) - n
  z = lst.count(0)
  return max(p,n,z,key=abs)

