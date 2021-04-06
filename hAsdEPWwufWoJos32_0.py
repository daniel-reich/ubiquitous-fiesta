
import re
def no_yelling(phrase):
  return re.sub("([!?])+$",r"\1",phrase)

