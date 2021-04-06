
import re
def find_longest(txt):
  txt = re.sub("[,.'\"]", " ", txt)
  return max((len(w), w.lower()) for w in txt.split())[1]

