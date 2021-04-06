
def is_heteromecic(n,a=0):
  if a*(a+1)==n:
    return True
  if a*(a+1)>n:
    return False
  return is_heteromecic(n,a+1)

