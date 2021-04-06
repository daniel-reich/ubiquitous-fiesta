
def repeated(s):
  ls = len(s)
  for i in range(2, ls//2 + 1):
    if ls % i == 0 and s == s[:i] * (ls//i):
      return True
  return False

