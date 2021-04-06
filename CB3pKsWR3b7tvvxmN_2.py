
def is_palindrome(txt):
  plaintxt = (''.join(filter(lambda c: c.isalpha(), txt))).lower()
  return plaintxt == plaintxt[::-1]

