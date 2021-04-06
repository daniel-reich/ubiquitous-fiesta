
import collections
def without_spaces(txt):
  return ''.join(txt.split(" "))
​
def can_build(txt1, txt2):
  txt1 = without_spaces(txt1)
  txt2 = without_spaces(txt2)
  for char in txt1:
    if not char in txt2:
      return False
  t1 = collections.Counter(txt1)
  t2 = collections.Counter(txt2)
  for char in t1.keys():
    if t1[char] > t2[char]:
      return False
  return True

