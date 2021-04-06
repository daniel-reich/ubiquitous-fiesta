
def balanced(lst):
  mid = len(lst)//2
  h1, h2 = lst[:mid], lst[mid:]
  if sum(h1) == sum(h2): return lst
  elif sum(h1) > sum(h2): return h1 + h1
  else: return h2 + h2

