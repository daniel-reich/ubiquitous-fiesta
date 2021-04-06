
def is_autobiographical(n):
  n = str(n)
  return all(n.count(str(idx)) == int(i) for idx, i in enumerate(n))

