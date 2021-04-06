
def find_odd(lst):
  a=[lst.count(x)%2!=0 for x in lst]
  return lst[a.index(True)]

