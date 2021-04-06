
def getSum(a, b):
  a, b = int(a), int(b)
  return (a + b)*(a - b + 1)//2
​
def is_astonishing(num):
  temp = str(num)
  a = ''
  b = ''
  if len(temp) == 2:
    a, b = temp[0], temp[1]
    resSum = getSum(b, a)
    if resSum == num:
      return "AB-Astonishing"
    return False
    
  for i in range(len(temp) - 1):
    a, b = temp[0: i+1], temp[i+1: len(temp)]
    if int(a) < int(b):
      resSum = getSum(b, a)
      if resSum == num:
        return "AB-Astonishing"
    else:
      resSum = getSum(a, b)
      if resSum == num:
        return "BA-Astonishing"
​
  return False

