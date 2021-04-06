
def missing(lst):
  delta = [lst[i] - lst[i-1] for i in range(1, len(lst))]
  delta = min(delta)
  
  for i in lst:
    n = i + delta
    if n not in lst:
      return n

