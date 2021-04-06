
def mult_table(n):
  
  table = []
  
  for m in range(1, n + 1):
    lst = []
    for o in range(1, n + 1):
      lst.append(m * o)
    table.append(lst)
  
  return table

