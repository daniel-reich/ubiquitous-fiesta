
def happy(n):
  if n==1: return True
  if n==4: return False
  return happy(sum(i**2 for i in map(int,str(n))))

