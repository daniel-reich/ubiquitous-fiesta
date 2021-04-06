
def is_heteromecic(n):
  if n == 0: True
  a = int(n**0.5)
  return a * (a + 1) == n

