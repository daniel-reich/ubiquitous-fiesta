
def func(lst):
  global res
  res = 0
  fun(lst)
  return res
​
def fun(lst):
  global res
  if isinstance(lst,list):
    res += len(lst)
    for l in lst:
      fun(l)

