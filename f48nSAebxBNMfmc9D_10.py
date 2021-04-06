
import re
def scrambled(words, mask):
  return [m.group(0) for m in [re.match('^' + mask.replace('*', '.') + '$', word) for word in words] if m != None]

