
import re
def validate(s):
  pattern = re.compile(r'((\+|)\d(\s|\/|\.|-|)|)(\(|)\d{3}(\)|)(\s|\/|\.|-|)\d{3}(\s|\/|\.|-|)\d{4}$')
  if re.match(pattern, s):
    return True
  else:
    return False

