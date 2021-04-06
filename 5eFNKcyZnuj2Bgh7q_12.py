
def is_automorphic(n):
  return str(n) == str(n**2)[-1 * len(str(n)):]

