
import re
def to_camel_case(txt):
  def capital(match):
    a,b = match.group(1,2)
    return b.upper()
  return re.sub(r'(_|\-)(\w)',capital,txt)

