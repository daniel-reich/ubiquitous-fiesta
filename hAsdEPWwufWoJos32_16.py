
import re
def no_yelling(phrase):
  a = re.findall('[.?!]+$', phrase)
  l = len(a[0]) - 1 if a else 0
  pattern = "[.?!]" + '{' + str(l) + '}$'
  return re.sub(pattern, "", phrase)

