
is_prime=lambda p:p>1and all(p%i for i in range(2,int(p**0.5+1)))
​
def cuban_prime(n):
  for y in range(n):
    if n==3*y**2+3*y+1 and is_prime(n):return str(n)+' is cuban prime'
  return str(n)+' is not cuban prime'

