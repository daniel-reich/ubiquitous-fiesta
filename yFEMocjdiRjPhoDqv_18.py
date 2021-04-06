
def prime_in_range(a, b):
  return bool(len(list(filter(lambda e: e and 2 in [e, 2**e % e], list(range(a, b+1))))))

