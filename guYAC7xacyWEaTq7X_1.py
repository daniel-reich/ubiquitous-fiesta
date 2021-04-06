
def is_autobiographical(n):
  n = str(n)
  return all(n.count(str(i)) == int(x) for i, x in enumerate(n))

