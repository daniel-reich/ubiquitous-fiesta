
import re
def cap_space(txt):
  return re.sub('[A-Z]', lambda x: ' '+x.group(0).lower(), txt)

