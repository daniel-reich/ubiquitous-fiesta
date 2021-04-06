
import re
​
open_ = r"^rgb(a)?\(\s*"
rgb = r"(25[0-5]|2[0-4]\d|1?\d?\d|100%|\d?\d%)"
comma = r"\s*,\s*"
alpha = r"\s*(?(1),\s*((?:0?\.\d*)?\d{1,3})\s*\)|\))?"
combined = "".join((open_, comma.join([rgb] * 3), alpha))
​
def valid_color (color):
  match = re.fullmatch(combined, color)
  if match is None:
    return False
  return True

