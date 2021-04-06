
import re
def make_happy(txt):
  regex = r'(?<=[:8x;])\('
  return re.sub(regex, ")" ,txt)

