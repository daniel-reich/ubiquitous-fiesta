
def all_prime(lst):
  return True if len(lst) == len([x for x in lst for i in range(2,x+1) if x%i == 0]) else False

