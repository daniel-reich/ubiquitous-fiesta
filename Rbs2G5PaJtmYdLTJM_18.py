
def is_heteromecic(n):
  for i in range(n+1):
    if i*(i+1) == n:
      return True
  return False

