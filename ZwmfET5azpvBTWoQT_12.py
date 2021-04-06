
import re
​
def valid_word_nest(word, nest):
  rgx = re.compile(word)
  while nest and len(rgx.findall(nest)) == 1:
    nest = nest.replace(word, '')
  return not nest

