
import re
def is_match(s, p):
  return bool(re.search(r'^{}$'.format(p),s))

