
import re
def same_length(txt):
  return all(len(a)==len(b) for a,b in zip(re.findall(r'1+',txt),re.findall(r'0+',txt))) and txt[-1]!='1'

