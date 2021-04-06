
import re
def remove_leading_trailing(n):
  return re.findall('[1-9]\d*?\.\d+[1-9]+|0\.\d*?[1-9]+',n)[0] if  bool(re.findall('\d+\.\d*?[1-9]+',n)) else str(round(float(n)))

