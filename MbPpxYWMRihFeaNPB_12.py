
def sum_of_evens(lst):
  inc = 0
  for i in lst:
    for j in i:
      if (j%2)==0:
        inc+=j
        
  return inc

