
import string
​
def invert(s):
  # your recursive solution here
  if len(s)==1:
    if s in string.ascii_uppercase:
      return s.lower()
    else:
      return s.upper()
  return invert(s[-1])+invert(s[:-1])

