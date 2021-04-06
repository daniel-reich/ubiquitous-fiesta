
def happy(n):
  if n == 1: return True
  if n == 4: return False
  return happy(sum(int(ch)**2 for ch in str(n)))

