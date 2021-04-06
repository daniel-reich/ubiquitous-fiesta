
def is_heteromecic(n):
  return n == 0 or len([i for i in range(1, n+1) if i * (i - 1) == n]) > 0

