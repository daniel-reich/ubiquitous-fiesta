
import re
​
def can_complete(initial, word):
  pattern = r'.*?'.join(initial)
  return bool(re.match(pattern, word))

