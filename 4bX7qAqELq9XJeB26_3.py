
import re
def to_camel_case(t):
  t = '' if t=='' else t.title() if t[0].isupper() else t[0] + t.title()[1:]
  return re.sub(r'[-_]','',t)

