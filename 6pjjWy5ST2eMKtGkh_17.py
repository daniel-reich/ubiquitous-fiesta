
import re
​
def replace(txt, r):
  pat = re.compile(r'[{0}]'.format(r))
  return pat.sub('#', txt)

