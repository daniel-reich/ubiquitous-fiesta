
import re
def is_alphabetically_sorted(sentence):
  no_pun = re.sub(r'[^\w\s]', '', sentence).lower()
  return any(''.join(sorted(w)) == w and len(w) > 2 for w in no_pun.split())

