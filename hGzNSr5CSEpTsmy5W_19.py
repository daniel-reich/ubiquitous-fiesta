
def not_good_math(n, k):
  c=0
  while c<k:
    if n%10:
      n-=1
      c+=1
    else:
      n//=10
      c+=1
  return n

