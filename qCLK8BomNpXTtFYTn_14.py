
def cumulative_sum(lst):
  
  a = 0
  b = []
  for i in lst:
    
    b.append(i + a)
    a += i
  
  return b

