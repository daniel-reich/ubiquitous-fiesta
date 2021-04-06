
def is_heteromecic(n):
  for x in range(n//2+1):
    if x*(x+1)==n:return 1
  return 0

