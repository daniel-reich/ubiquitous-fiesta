
import re
def retrieve(txt):
  if len(txt) == 0:
    return []
  return [re.sub(r'[^a-z]', '', word) for word in txt.lower().split(' ') if word[0] in 'aeiou']

