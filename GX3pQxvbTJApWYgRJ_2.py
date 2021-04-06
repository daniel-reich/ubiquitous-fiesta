
def is_kaprekar(n):
  s = str(n ** 2)
  i = len(s) // 2
  return n == int(s[:i] or 0) + int(s[i:])

