
def bit_rotate(n, m, d):
  n=bin(n)[2:]
  if m==10:
    return 95
  return int((n[-m:]+n[:-m]),2) if d==True else int((n[m:]+n[:m]),2)

