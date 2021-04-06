
def factorial(n):
  result = 1
  num = n
  myRange = range(num + 1)
​
  for index, item in enumerate(myRange, start=1):
    lastItem = myRange[len(myRange) - index]
​
    if lastItem == 0:
      pass
    else:
      result *= lastItem
      continue
  
  return result

