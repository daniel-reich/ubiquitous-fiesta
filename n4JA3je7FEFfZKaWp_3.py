
def million_in_month(first_month, multiplier):
  goal=1000000
  balance=0
  n=0
  print(first_month)
  print(multiplier)
  while balance<goal:
    n=n+1
    balance = balance +first_month
    first_month=first_month*multiplier
    
  print(n)
  return n

