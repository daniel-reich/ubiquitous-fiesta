
import re
def can_complete(initial, word):
  return bool(re.search('.*'.join(list(initial)), word))

