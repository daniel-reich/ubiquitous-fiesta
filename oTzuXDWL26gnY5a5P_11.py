
def prime_numbers(num):
  count=0
  for i in range(2,num+1):
    if prime(i):
      count+=1
  return count
def prime(n):
  if n == 2:
    return True
  else:
    for i in range(2,n):
      if n%i == 0:
        return False
    return True

