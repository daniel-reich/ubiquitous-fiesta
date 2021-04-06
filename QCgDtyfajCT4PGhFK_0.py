
def is_prime (n):
  for x in range (2,n):
    if n%x==0:
      return False
  return True
​
def prime_factorization(number):
  lista=[]
  for x in range (2,number+1):
    if is_prime(x):
      while number%x==0:
        lista.append(x)
        number=number//x
  return lista

