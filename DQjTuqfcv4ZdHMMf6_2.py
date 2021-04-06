
def kaprekar(n, i = 0):
​
  if n == 6174: return i
    
  s = (str(n) + '0')[:4]
  
  smaller = int(''.join(sorted(s)))
  bigger = int(''.join(sorted(s)[::-1]))
  
  return kaprekar(bigger-smaller, i+1)

