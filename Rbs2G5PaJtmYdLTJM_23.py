
def is_heteromecic(n):
  if n:
    k=1
    i=1
    while k<n:
      k=i*(i+1)
      i+=1
    if k==n:
      return True
    else:
      return False
  return True

