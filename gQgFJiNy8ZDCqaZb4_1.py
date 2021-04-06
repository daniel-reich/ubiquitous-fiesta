
import re
​
def overlap(s1, s2):
  return re.sub(r'(\w*) \1', r'\1', '{} {}'.format(s1, s2))

