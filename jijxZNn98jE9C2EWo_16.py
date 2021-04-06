
def automorphic(n):
  return str(n) == str(n * n)[-len(str(n)):]

