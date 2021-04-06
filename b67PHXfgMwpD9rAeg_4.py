
import re
def plus_sign(txt):
  return len(re.findall(r'(?=(\+[a-zA-Z]\+))',txt)) == sum(1 for i in txt if i.isalpha())

