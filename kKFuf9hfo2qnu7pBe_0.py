
def is_prime(p,n,l=0,r=None):
  r=len(p)-1
  while r>=l:
    m=l+(r-l)//2
    if p[m]==n:return'yes'
    elif p[m]>n:r=m-1 
    else:l=m+1
  return'no'

