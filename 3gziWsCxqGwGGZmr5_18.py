
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
​
​
def fat_prime(a, b):
  try:
    return max(i for i in range(min(a, b), max(a, b)) if is_prime(i) == True)
  except ValueError:
    return 'No prime found'

