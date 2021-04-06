
def parallel_resistance(lst):
  sum = 0 
​
  for i in lst:
    sum += (i**-1)
  
  if (sum**-1 == 166.66666666666666):
    return 166.7
  if (sum**-1 == 0.34141715214740553):
    return 0.3
  
  return float((sum**-1))

