
def closest_palindrome(n):
  a = n
  b = n
  if str(n) == str(n)[::-1]:
    return n
  while True:
    a += 1
    b -= 1
    if str(a) == str(a)[::-1] and str(b) == str(b)[::-1]:
      return min(a, b)
    if str(a) == str(a)[::-1]:
      return a
    if str(b) == str(b)[::-1]:
      return b

