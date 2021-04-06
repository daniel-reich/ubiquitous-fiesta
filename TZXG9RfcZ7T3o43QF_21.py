
import re
def same_length(txt):
  m = re.findall("1+0+",txt)  
  return False if not m else all(i.count('1')==i.count('0') for i in m)  and len("".join(i for i in m))==len(txt)

