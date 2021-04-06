
def is_kaprekar(n):
  n_str = str(n ** 2)
  if len(n_str) == 1:
    half1 = 0
  else:
    half1 = n_str[: len(n_str) // 2]
  half2 = n_str[len(n_str) // 2 :]
  return int(half1) + int(half2) == n

