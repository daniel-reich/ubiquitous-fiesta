
def lychrel(n,i=0):
  if str(n)==str(n)[::-1]:
    return i
  if i == 500:
    return True
  return lychrel(n+int(str(n)[::-1]),i+1)

