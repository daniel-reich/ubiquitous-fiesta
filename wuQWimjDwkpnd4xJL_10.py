
def balanced(lst):
  print(len(lst)/2-1)
  a, b = lst[(len(lst)//2):], lst[:(len(lst)//2)]
  return lst if sum(a)==sum(b) else a+a if sum(a)>sum(b) else b+b

