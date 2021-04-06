
def almost_palindrome(txt):
  rev = txt[::-1]
  if txt == rev: return False
  return sum(1 for a,b in zip(txt, rev) if a != b) == 2

