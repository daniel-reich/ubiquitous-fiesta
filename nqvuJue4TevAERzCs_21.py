
import re
def has_digit(txt):
  x = re.search("[0-9]", txt)
  print(x)
  return x != None

