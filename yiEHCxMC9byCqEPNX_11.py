
from string import ascii_lowercase
def is_palindrome(p):
  if len(p) == 0 or len(p) == 1:
    return True
  if p[0].lower() not in ascii_lowercase:
    return is_palindrome(p[1:])
  if p[-1].lower() not in ascii_lowercase:
    return is_palindrome(p[:-1])
  if p[0].lower() == p[-1].lower():
    return is_palindrome(p[1:-1])
  return False

