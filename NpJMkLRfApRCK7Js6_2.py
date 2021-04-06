
def is_palindrome(w):
  return True if len(w) < 2 else False if \
    w[0] != w[-1] else is_palindrome(w[1:-1])

