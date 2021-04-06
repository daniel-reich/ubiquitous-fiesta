
def possible_palindrome(txt):
  x = 0
  for i in set(txt):
    if txt.count(i)%2 != 0:
      x += 1
  return False if x>1 else True

