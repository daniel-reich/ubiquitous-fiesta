
def is_prime(number):
  if number==1: return False
  for i in range(2,number):
    if number%i==0: return False
  return True
def all_prime(lst):
  ls  = [True if is_prime(element) else False for element in lst]
  return all(ls)

