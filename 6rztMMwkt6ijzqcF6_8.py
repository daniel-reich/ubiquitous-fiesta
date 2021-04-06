
import re
​
def is_repeated(strn):
  try:
    return len(strn) / len(re.fullmatch(r"(.+?)\1+", strn).group(1))
  except AttributeError:
    return False

