
def all_prime(lst):
  x = [x for x in lst if x>1 and all(x%i for i in range(2, x))]
  return True if len(x) == len(lst) else False

