
def is_heteromecic(n, i=0):
  # your recursive solution here
  if i*(i+1) == n:
    return True
  if n == i:
    return False
  i+=1
  return is_heteromecic(n, i)

