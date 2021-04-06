
def all_prime(lst):
  
  return len([s for s in lst if s>1 and all(s%m for m in range(2,s))])==len(lst)

