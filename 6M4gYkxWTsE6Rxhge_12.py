
def all_prime(lst):
  return False if 1 in lst else len([i for i in lst if all(i%n for n in range(2, i))])==len(lst)

