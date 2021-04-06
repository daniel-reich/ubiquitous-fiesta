
import re
def no_yelling(phrase):
  return re.sub('\?+$', '?', re.sub('\!+$', '!', phrase))

