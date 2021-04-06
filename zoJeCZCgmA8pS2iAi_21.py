
def func_sort(lst):
  s1= lambda x: s1(x())+1 if callable(x)else 0
  return sorted(lst,key=s1)

