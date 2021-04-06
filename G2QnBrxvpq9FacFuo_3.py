
import re
def possible_path(lst):
  s=''.join([str(x) for x in lst])
  return not bool(re.search('\d\d', s))

