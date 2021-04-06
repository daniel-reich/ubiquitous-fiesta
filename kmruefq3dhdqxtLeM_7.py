
def sum_digits(a, b):
  tot = 0
  
  for num in range(a, b+1):
    tot += sum(int(i) for i in list(str(num)))
    
  return tot

