
import re
​
def valid_name(name):
  return bool(re.match(r'(([A-Z][a-z]+) ([A-Z][a-z]+ |[A-Z]\. )|[A-Z]\. ([A-Z]\. )?)[A-Z][a-z]+$', name))

