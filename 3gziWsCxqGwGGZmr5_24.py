
def fat_prime(a, b):
  h = [max(a,b), min(a,b)]
  for i in range(h[0], h[1], -1):
    if all(i % x != 0 for x in range(2,i)):
      return i

