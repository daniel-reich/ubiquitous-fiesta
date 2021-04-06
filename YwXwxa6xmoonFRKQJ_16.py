
def josephus(n):
  if n==0:
    return False
  if n==1:
    return 0
  else:
    return (josephus(n-1)+2)%n

