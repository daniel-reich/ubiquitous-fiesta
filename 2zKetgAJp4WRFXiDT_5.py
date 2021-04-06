
def number_length(n):
  out = 0
  while n >= 1:
    n /= 10
    out += 1
  if n == 0: out += 1
  return out

