
def is_automorphic(n):
  return str(n) == str(n**2)[-len(str(n)):]

