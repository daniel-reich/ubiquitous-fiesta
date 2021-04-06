
import string
​
def cap_to_front(s):
  s1 = [c for c in s if c in string.ascii_uppercase]
  s2 = [c for c in s if c in string.ascii_lowercase]
  return ''.join(s1 + s2)

