
import re
def plus_sign(txt):
  return all([True if re.search('[+0-9]',txt[i]) else False for i in range(0,len(txt),2)])

