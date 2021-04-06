
from string import ascii_letters
​
def is_palindrome(p):
  # clean up the string (we may be doing it again)
  p = "".join([c for c in p if c in ascii_letters]).lower()
  # an empty string or a single character is a palindrome 
  if len(p) < 2:
    return True
  # if first and last don't match, return False
  if p[0] != p[-1]:
    return False
  # otherwise, check the middle
  return is_palindrome(p[1:-1])

