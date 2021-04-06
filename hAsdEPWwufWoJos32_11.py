
import re
def no_yelling(phrase):
  start = re.match("[\w\s\W]+[\w]", phrase).group(0)
  end = phrase[-1]
  return start + end

