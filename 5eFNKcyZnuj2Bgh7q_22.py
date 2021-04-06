
def is_automorphic(n):
  return str(n ** 2)[-len(str(n)):] == str(n)[-len(str(n)):]

