
from decimal import *
def fractions(decimal):
  pattern = decimal.split('(')[1].split(')')[0]
  number = Decimal(decimal.split('(')[0]+pattern)
  non_rep_count = len(decimal.split('(')[0].split('.')[1]) 
  rep_count =len(pattern)
  number1 = number *10**(non_rep_count)
  number2 = number * 10**(non_rep_count+rep_count) + Decimal('0.'+pattern)
  div=gcd(int(number2-number1),(10**(non_rep_count+rep_count)-10**(non_rep_count)))
  return str(int(int(number2-number1)/div)) + \
  '/' + str(int((10**(non_rep_count+rep_count)-10**(non_rep_count))/div))
​
def gcd(n1, n2):
  while n2:
    n1, n2 = n2, n1 % n2
  return n1

