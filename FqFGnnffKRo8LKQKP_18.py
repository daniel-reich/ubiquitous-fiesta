
def is_simple(n):
  m = n
  lst = []
  total = 0
  
  while m:
    lst.append(m % 10)
    m //= 10
  for i, j in enumerate(lst[::-1], 1):
    total += j ** i
    
  return total == n
​
def simple_numbers(a, b):
  return [x for x in range(a, b + 1) if is_simple(x)]

