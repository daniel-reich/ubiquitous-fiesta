
def add_odd_to_n(n):
  out = 0
  for i in range(n+1):
    if i%2==1:
      out+=i
  return out

