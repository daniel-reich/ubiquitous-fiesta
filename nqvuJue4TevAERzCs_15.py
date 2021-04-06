
import re
def has_digit(txt):
  tester = re.findall("[0-9]", txt)
  tester = ''.join(tester)
  if tester.isalnum():
    return True
  else:
    return False

