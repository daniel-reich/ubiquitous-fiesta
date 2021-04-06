
def is_palindrome(txt):
  x = ''.join(e.lower() for e in txt if e.isalnum())
  return x==x[::-1]

