
def is_prime(x):
  return all(x % i for i in range(2, x)) and x >= 2
​
​
def all_prime(lst):
  return all(map(is_prime, lst))

