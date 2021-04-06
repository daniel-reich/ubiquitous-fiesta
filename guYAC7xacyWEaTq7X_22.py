
def is_autobiographical(n):
  n = str(n)
  for i in range(0, len(n)):
    if n.count(str(i)) != int(n[i]):
      return False
  return True

