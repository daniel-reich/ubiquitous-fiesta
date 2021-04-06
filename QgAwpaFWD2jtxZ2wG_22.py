
def sum_digits(n):
  cont=0
  while n>=1:
    n/=10
    cont+=1
  return 1 if n==0 else cont

