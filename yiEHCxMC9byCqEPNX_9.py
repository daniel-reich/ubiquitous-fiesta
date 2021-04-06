
def is_palindrome(p):
  p = ''.join([x.lower() for x in p if x.isalpha()])
  return True if len(p) <= 1 else False if p[0] != p[-1] else is_palindrome(p[1:-1])

