
import re
def is_palindrome(txt):
  a = re.sub(r',|!|-', '', txt)
  b = a.replace(' ', '')
  return b.lower() == b[::-1].lower()

