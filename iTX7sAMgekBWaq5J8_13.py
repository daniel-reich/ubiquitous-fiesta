
def addUpTo(num):
  result = 1
  for i in range(num + 1): 
    result = i*(i+1)/2
  return int(result)

