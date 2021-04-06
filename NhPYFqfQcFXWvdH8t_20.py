
def euclid(a,b):
  s,o_s=0,1
  t,o_t=1,0
  r, o_r=b,a
  while r:
    q=o_r//r
    o_r, r=r, o_r-q*r
    o_s, s=s, o_s-q*s
    o_t, t=t, o_t-q*s
  return [o_r, o_s, o_t]  
def mod_inv(n, m):
  g, x, y=euclid(n,m)
  if g!=1:
    return False
  else:
    if x<0:
      x+=m
    return x

