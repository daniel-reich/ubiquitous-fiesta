
import re
​
def convert_binary(string):
  return "".join(["0" if re.match(r"[A-Ma-m]", x) else "1" for x in string])

