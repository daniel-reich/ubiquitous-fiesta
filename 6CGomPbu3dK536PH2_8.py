
def accumulating_list(lst):
  a = []
  for i in range(0, len(lst)):
    b = 0
    for j in range(0,i+1):
      b += lst[j]
    a.append(b)
  return a

