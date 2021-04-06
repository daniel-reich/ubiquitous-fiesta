
def accumulating_list(lst):
  inc=0
  l=[]
  for i in lst:
    inc+=i
    l.append(inc)
  return l

