
def is_palindrome(txt):
  txt=[c for c in txt.lower() if c.isalpha()]
  return txt==txt[::-1]

