
import re
def find_longest(s):
  if type(s) == str:
    s = re.split(r'[^a-zA-Z]+',s)
  return s[0].lower() if len(s) == 1 or len(s[0]) >= len(find_longest(s[1::])) else find_longest(s[1::])

