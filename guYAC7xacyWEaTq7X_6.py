
def is_autobiographical(n):
  n = str(n)
  bd = {i:int(n[i]) for i in range(len(n))}
  return all(bd.get(i) == n.count(str(i)) for i in range(len(n)))

