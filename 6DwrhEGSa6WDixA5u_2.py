
def is_narcissistic(n):
  s=str(n)
  l = len(s)
  total = 0
  for i in s:
    total += int(i)**l
  return total == n

