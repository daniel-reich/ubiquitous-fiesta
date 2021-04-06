
import re
def to_snake_case(txt):
  return "".join(re.sub(r"[A-Z]",lambda m:"_"+m.group()[0].lower(),txt))
​
def to_camel_case(txt):
  return "".join([i for i in re.sub(r"[_].",lambda m:m.group()[1].upper(),txt)])

