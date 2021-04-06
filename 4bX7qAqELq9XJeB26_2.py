
import re
​
def to_camel_case(text):
  return re.sub('[\W_](\w)', lambda m: m.group(1).upper(), text)

