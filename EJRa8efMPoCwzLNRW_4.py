
import re
def dakiti(s):
  lst = sorted(s.split(), key=lambda w: int(re.sub(r'\D', '', w)))
  return ' '.join(re.sub('\d', '', w) for w in lst)

