
import re
def validate(s):
    ns = re.findall(r'\+?[1]?[ -]?[\(./]?[\d]{3}[\)]?[ -./]?[\d]{3}[ -./]?[\d]{4}',s)
    if not ns:
      return False
    return ns[0] == s

