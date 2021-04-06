
def all_prime(lst):
  return all(is_prime(num) for num in lst)
  
def is_prime(num):
  if num == 1: return False
  for i in range(2,num):
    if num % i == 0: return False
  return True

