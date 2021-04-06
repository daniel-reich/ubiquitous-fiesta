
import re
def to_snake_case(txt):
  pattern = re.compile(r"([a-z])([A-Z])")
  match = pattern.sub(r'\1_\2', txt).lower()
  return match
  
​
def to_camel_case(txt):
  pattern = re.compile(r"(_)([a-z])")
  match = pattern.sub(lambda x: x.group(2).upper(), txt)
  a = re.sub(r"_", "", match)
  return a

