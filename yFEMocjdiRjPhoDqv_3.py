
def prime_in_range(n1, n2):
  for i in range(n1,n2+1):
    is_prime=True
    for j in range(2,i):
      if i%j!=0 and is_prime==True:
        is_prime=True
      else:
        is_prime=False
    if is_prime==True:
      return True
  return False

