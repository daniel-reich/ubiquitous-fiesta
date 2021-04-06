
import re
def absolute(txt):
  pat = re.compile(r'(?!=\w)a(?!\w)',re.I)
  return pat.sub('an absolute',txt).capitalize()

