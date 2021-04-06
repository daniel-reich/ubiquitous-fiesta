
def snakefill(n):
  l = 1; c = 0
  while l<(n**2):
    l+=l; c+=1
  return c if l<=n**2 else c-1

