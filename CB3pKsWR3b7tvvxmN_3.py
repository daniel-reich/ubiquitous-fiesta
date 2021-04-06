
def is_palindrome(txt):
  b=""
  a="abcdefghijklmnopqrstuvwxyz"
  for x in txt:
    if x.lower() in a:
      b+=x.lower()
  if b == b[::-1]:
    return True
  return False

