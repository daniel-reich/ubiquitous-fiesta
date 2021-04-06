
import re
def super_reduced_string(txt):
  while re.findall(r'(\w)(\1)', txt):
    for i in re.findall(r'(\w)(\1)', txt):
      txt = txt.replace(''.join(i), '')
  return txt if txt else 'Empty String'

