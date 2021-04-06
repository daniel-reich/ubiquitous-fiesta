
def move_zeros(lst):
  a = []
  b = []
  for i in lst:
    if i != 0 or i is False:
      a.append(i)
    else: 
      b.append(i)
  
  return a + b

