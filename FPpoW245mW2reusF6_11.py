
def even_last(lst):
  total = 0
  if len(lst)==0:
    return 0
  for i in range(len(lst)):
    if i%2==0:
      total+=lst[i]*lst[-1]
  return total

