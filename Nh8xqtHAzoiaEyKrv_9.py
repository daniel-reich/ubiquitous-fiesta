
import re
​
def correct_sentences(txt):
  first, *rest = ' '.join(txt.split())
  return first.upper() + re.sub(' ([A-Z])', r'. \1', ''.join(rest)) + '.'

