
import re
def is_authentic_skewer(s):
  return bool(re.match(r'^([BCDFGHJKLMNPQRSTVWXYZ](-+)[AEIOU]\2)+[BCDFGHJKLMNPQRSTVWXYZ]$', s))

