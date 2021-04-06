
def parity_analysis(num):
  return num%2 == sum_digits(num)%2
  
def sum_digits(n):
  total = 0
  while n > 0:
    total += n%10
    n //= 10
  return total

