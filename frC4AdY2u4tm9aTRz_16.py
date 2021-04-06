
def standard_deviation(lst):
  sum_ = sum(lst)
  mean = sum_ / len(lst)
  
  dev = 0
  for i in range(len(lst)):
    dev += (lst[i] - mean)**2
    
  median = (dev / len(lst))**0.5
  
  return round(median , 2)

