
import re
def space_message(txt):
  while '[' in txt:
    txt = re.sub(r'\[(\d)([A-Z]+)\]',lambda m: m.group(2)*int(m.group(1)),txt)
  
  return txt

