
def show_the_love(lst):
  y = 0
  for x in range(len(lst)):
    y += (lst[x]/4)
    lst[x]-=lst[x]/4
  i = smallOne(lst)
  lst[i] += y
  return lst
  
def smallOne(lst):
  small = 100000
  i = 0
  for x in range(len(lst)):
    if lst[x] < small:
      small = lst[x]
      i = x
  return i

