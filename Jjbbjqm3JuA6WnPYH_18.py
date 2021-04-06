
def bit_rotate(n, m, d):
  n=bin(n)[2:]
  while m:
    if d:n=n[-1]+n[:-1]
    else:n=n[1:]+n[0]
    m-=1
  return int(n,2)

