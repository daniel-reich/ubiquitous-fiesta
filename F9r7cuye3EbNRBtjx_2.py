
from re import sub
def string_builder(s):
  s = sub(r'(\d+)(\[)([^\[\]]+)(\])',lambda x: int(x.group(1)) * x.group(3),s)
  if '[' in s:
    return string_builder(s)
  return s

