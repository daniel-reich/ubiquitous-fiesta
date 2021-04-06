
def logarithm(base, num):
​
  if base <=1 or num <= 0:
    return "Invalid"
    
  count = 1
  temp = base
  
  while temp < num:
    temp = temp * base
    count += 1
    
  return count

