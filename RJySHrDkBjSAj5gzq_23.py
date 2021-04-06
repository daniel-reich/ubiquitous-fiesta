
def fct(n):
  return 1 if n <= 1 else n * fct(n-1)
​
def nespers(lst):
  perms = fct(len(lst))
  for i in lst:
    if type(i) == list: perms *= nespers(i)
  return perms

