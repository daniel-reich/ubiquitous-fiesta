
import re
​
def lambda_to_def(code):
  strings = re.findall("'[^']*'", code)
  code = re.sub("'[^']*'", "@", code)
  
  a, b = code.split(":", 1)
  a = a.split(" ", 3)
  
  res = "def " + a[0] + "(" + a[3] + "):\n\treturn" + b
  return re.sub("@", lambda _: strings.pop(0), res)

