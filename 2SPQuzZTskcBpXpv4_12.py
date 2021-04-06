
def euclidean(a, b):
  if a < b:
    a, b = b, a
  for i in reversed(range(1, b + 1)):
    if a % i == 0: 
      if b % i == 0:
        return i

