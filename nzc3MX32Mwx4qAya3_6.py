
def ranged_reversal(lst, start, finish):
  x=[lst[i] if not i in range(start,finish+1) else 0 for i in range(len(lst))]
  y=[lst[i] for i in range(start,finish+1)]
  for i in range(start,finish+1):
    x[i]=y.pop()
  return x

