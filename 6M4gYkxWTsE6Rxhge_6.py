
def prime_num(n):
​
  if n > 1:
    for i in range(2, n):
      if n % i == 0:
        return False
    return True
  else:
    return False
​
​
​
def all_prime(lst):
  ans = [prime_num(i) for i in lst]
  return all(ans)

