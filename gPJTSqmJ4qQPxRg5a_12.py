
def func(num):
  sum = 0
  for i in str(num):
    sum += (int(i) - len(str(num)))
    
  return sum

