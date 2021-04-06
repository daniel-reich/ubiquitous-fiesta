
from string import ascii_lowercase
def base_conv(n, b):
  if isinstance(n, int):
    res = ""
    while n > 0:
      res = ascii_lowercase[n % b] + res
      n //= b
    return res
  # Not int- str
  res = 0
  try:
    for i, ch in enumerate(n[::-1]):
      res += ascii_lowercase[: b].index(ch) * b ** i
  except:
    return "%s is not a base %i number." % (n, b)
  return res

