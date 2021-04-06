
def max_product(n):
  def prod_of_digits(n):
    prod = 1
    
    s = str(n)
    
    for digit in s:
      prod *= int(digit)
    
    return prod
  
  maxprod = 0
  maxdigits = []
  
  for num in range(1, n+1):
    prod = prod_of_digits(num)
    if prod > maxprod:
      maxdigits = [num]
      maxprod = prod
    elif prod == maxprod:
      maxdigits.append(num)
  
  return maxdigits

