
def lychrel(n):
  for i in range(501):
    s = str(n)
    if s == s[::-1]: 
      return i
    n = n + int(s[::-1])
  return True

