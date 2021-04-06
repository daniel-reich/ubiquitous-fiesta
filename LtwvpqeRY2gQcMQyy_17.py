
import re
def sig_figs(num):
  add = '' if '.' in num else '[1-9]'
  meh = re.findall('^[1-9]$|[1-9]\d*{}'.format(add), re.sub('\.','',num))
  return len(meh[0]) if meh else 0

