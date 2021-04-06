
def is_automorphic(n):
  string = str(pow(n,2))
  return n == int(string[-len(str(n)):])

