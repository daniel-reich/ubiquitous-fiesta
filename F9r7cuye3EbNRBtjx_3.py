
import re
def string_builder(s):
  while bool(re.search(r'(\d+)\[([^\d\]]+)\]',s)):
    s=re.sub(r'(\d+)\[([^\d\]]+)\]', lambda m:m.group(2)*int(m.group(1)), s)
  return s

