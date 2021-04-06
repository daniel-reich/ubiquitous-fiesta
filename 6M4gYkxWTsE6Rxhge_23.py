
def is_prime(num):
  if num==1:
    return False
  i=2
  while i*i<=num:
    if num%i==0:
      return False
    i+=1
  return True
​
def all_prime(lst):
  return all(is_prime(i) for i in lst)

