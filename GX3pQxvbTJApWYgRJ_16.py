
def is_kaprekar(n):
  v = str(n * n)
  if len(v) == 1:
    return int(v) == n
  return int(v[:len(v) // 2]) + int(v[len(v) // 2:]) == n

