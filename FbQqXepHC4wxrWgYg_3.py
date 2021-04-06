
def is_prime(n):
  if n < 2:
    return False
  else:
    faktor = 1
    for i in range(1,n):
      if n%i == 0:
        faktor += 1
    if faktor == 2:
      return(True)
    else:
      return(False)
​
def prime_divisors(num):
  divisors = []
  prime_div = []
  for i in range(1,num+1):
    if num%i == 0:
      divisors.append(i)
  for j in divisors:
    if is_prime(j):
      prime_div.append(j)
  return(prime_div)

