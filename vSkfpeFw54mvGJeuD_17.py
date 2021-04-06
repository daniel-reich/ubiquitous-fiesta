
def lychrel(n):
  for x in range(500):
    if str(n)==str(n)[::-1]: return x
    n+=int(str(n)[::-1])
  return True

