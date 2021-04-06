
def is_palindrome(txt):
  y = [i.lower() for i in txt if i.isalpha()]
  return y == y[::-1]

