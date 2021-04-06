
def closing_in_sum(n):
  n=str(n)
  a=n[:len(n)//2]
  b=n[-(len(n)//2):][::-1]
  total=0
  for i in range(len(a)):
    total+=int(a[i]+b[i])
  if len(n)%2:total+=int(n[len(n)//2])
  return total

