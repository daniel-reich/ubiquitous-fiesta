
def is_autobiographical(n):
  for i in range(len(str(n))):
    if str(n).count(str(i)) != int(str(n)[i]):
      return False
  return True

