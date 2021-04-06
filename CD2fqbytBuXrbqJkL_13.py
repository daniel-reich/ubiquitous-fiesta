
from collections import Counter
​
def can_build(txt1, txt2):
  return not [1 for a in Counter(txt1.replace(' ', '')) if Counter(txt2)[a] < Counter(txt1.replace(' ', ''))[a]]

