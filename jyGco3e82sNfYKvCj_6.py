
def rev(n):
  n = str(n)
  if n[0] == '-':
    n = n[1:]
    return n[::-1]
  return n[::-1]

