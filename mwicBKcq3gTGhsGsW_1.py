
import re
​
def make_word_riddle(txt):
  return re.sub('(\w+)in(\w)(\w+)', r'\2\1\3', txt.lower()).upper()

