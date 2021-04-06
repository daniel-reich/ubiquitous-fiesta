
import re
def super_reduced_string(txt):
  if re.compile(r'(\w)\1{1}').findall(txt):
    return super_reduced_string(re.sub(r'(\w)\1{1}', '', txt))
  else:
    return txt if txt else 'Empty String'

