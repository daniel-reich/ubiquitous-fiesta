
import re
def remove_leading_trailing(n):
  exp = r'(0\.\d*[1-9])|([1-9]\d*(\.\d*[1-9])?)'
  match = re.search(exp, n)
  if match:
    return match.group()
  else:
    return "0"

