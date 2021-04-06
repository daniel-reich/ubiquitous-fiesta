
import re
​
def correct_sentences(s):
  s = re.sub(" +(?=[A-Z])", ". ", s.strip())
  s = re.sub(" +", " ", s)
  return s[0].upper() + s[1:] + "."

