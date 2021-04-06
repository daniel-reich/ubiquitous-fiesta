
import re
def valid_color (color):
  return bool(re.match("rgb(a)?\((,?((?=\d{1,3}\%)(100|\d{1,2})\%|(25[0-5]|1?\d{1,2}))){3}(?(1),(1\.0*|0?\.?\d+))\)", "".join(color.split()))) and (color.startswith("rgb(") or color.startswith("rgba("))

