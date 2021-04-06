
def fat_prime(a, b):
  c = []
  for i in range(max(b,a), min(a,b), -1):
      for j in range(2, i):
          if i%j==0:
              break
      else:
          c.append(i)
          break
  return c[0]

