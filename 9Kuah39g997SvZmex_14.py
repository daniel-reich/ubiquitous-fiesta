
import re
def common_last_vowel(txt):
  a = [w[-1] for w in re.compile('[^aeiou ]').sub('',txt.lower()).split()]
  return max(a, key=a.count)

