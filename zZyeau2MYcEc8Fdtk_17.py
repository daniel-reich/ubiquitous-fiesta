
def round_number(num, n):
  a = b = num
  while a % n: a += 1
  while b % n: b -= 1
  if abs(num-a) == abs(num-b): return max(a, b)
  return a if abs(num-a) < abs(num-b) else b

