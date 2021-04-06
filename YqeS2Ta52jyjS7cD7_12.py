
def is_prime(n):
  try: return n > 1 and not any([i for i in range(2, n//2+1) if n % i == 0])
  except: return False

