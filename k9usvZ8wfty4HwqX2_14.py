
def cuban_prime(num):
  for i in range(num):
    cur = cuban_eq(i,i+1)
    if cur==num and is_prime(cur):
      return '{0} is cuban prime'.format(num)
  return '{0} is not cuban prime'.format(num)
  
​
def cuban_eq(x,y):
  return (pow(x,3) - pow(y,3))/(x - y)
​
def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

