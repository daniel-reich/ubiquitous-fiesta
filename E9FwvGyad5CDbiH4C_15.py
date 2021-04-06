
def block(lst):
  blocked = 0
  for i in range(len(lst)):
    blocked += lst[i].count(2) * (len(lst) - (i+1))
  
  return blocked

