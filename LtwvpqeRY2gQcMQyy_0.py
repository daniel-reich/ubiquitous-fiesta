
import re
​
def sig_figs(num):
  return len(re.sub(r'(?<=[1-9])(0+)\Z', '', num).lstrip('-0.').replace('.', ''))

