
def product(lst):
  a = max(lst)
  while lst.count(a) > 0 and len(lst) != lst.count(a):
    lst = lst[:lst.index(a)] + lst[lst.index(a)+1:]  
  c = max(lst)
  return a*c

