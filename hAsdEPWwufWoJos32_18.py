
import re
def no_yelling(phrase):
  end = re.search(r'[?!]{2,}$', phrase)
  return re.sub(r'[?!]{2,}$', end.group()[0], phrase) if end else phrase

