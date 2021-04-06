
def count(n):
  if abs(n) < 10:
    return 1
  else:
    return count(abs(n)//10) + 1

