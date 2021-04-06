
import re
def camelCasing(s):
  r = re.split(r'[ _]', s)
  return r[0].lower() + ''.join(x.capitalize() for x in r[1:])

