
def order_people(lst, people):
  if lst[0]*lst[1] < people:
    return "overcrowded"
  a =[]
  flag = 0
  inp = [x for x in range(1,people+1)]
  for i in range(0,lst[0]):
    a.append([])
    for j in range(0,lst[1]):
      if len(inp) != 0 and flag == 0:
        a[i].append(inp.pop(0))
      elif len(inp) != 0 and flag == 1:
        a[i][:0] = [inp.pop(0)]
      elif len(inp) == 0 and flag == 1:
        a[i][:0] = [0]
      else:
        a[i].append(0)
        
    if flag == 1:
      flag = 0
    else:
      flag = 1
  return a

