
def is_heteromecic(n):
  for i in range(int(n**0.5)+1):
    if i*(i+1) == n:
      return True
  return False

