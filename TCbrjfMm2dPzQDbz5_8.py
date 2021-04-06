
import re
def insert_whitespace(txt):
  pattern = re.compile(r'[A-Z][a-z]+')
  matches = pattern.findall(txt)
  return " ".join(matches)

