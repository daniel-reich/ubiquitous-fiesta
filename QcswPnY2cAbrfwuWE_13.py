
def filter_factorials(numbers):
  
  index = 0
  divider = 1
  n = numbers[index]
  res = []
​
  while True:
​
    if not (n % divider):
      n //= divider
    else:
​
      if n == 1:
        res.append(numbers[index])
        
      divider = 1
      index += 1
      
      if index == len(numbers):
        break
      else:
        n = numbers[index]
        continue
​
    divider += 1
​
  return res

