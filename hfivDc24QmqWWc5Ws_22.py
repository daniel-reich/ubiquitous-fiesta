
def check_prime(num):
  if num == 2 or num == 3: return True
  for i in range(2,num):
    if num % i ==0:
      return False
  return True
  
def eratosthenes(num):
  L = []
  for i in range(2,num+1):
    if check_prime(i):
      L.append(i)
  return L

