
import re
def to_snake_case(txt):
  pattern = re.compile(r'([A-Z])')
  matches = pattern.finditer(txt)
  for m in matches:
    txt =  re.sub(m.group(), '_'+m.group().lower(), txt)
  return txt
  
​
def to_camel_case(txt):
  pattern = re.compile(r'_([a-z])')
  matches = pattern.finditer(txt)
  for m in matches:
    txt =  re.sub(m.group(), m.group(1).upper(), txt)
  return txt

