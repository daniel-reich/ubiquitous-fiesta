
import re
def same_length(txt):
  matches = zip(re.findall(r'1+', txt), re.findall(r'0+', txt))
  return all(len(a)==len(b) for a,b in matches) and len(txt) % 2 == 0

