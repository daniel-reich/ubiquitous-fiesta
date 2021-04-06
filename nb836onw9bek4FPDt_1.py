
import re
def count_same_ends(txt):
  return sum(t[0]==t[-1] if len(t)>1 else 0 for t in re.sub('[^a-z\s]','',txt.lower()).split())

