
def lychrel(n):
  for i in range(500 + 1):
    sn = str(n)
    if sn == sn[::-1]: return i
    n += int(sn[::-1])
    
  return True

