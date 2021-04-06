
# resources: https://stackoverflow.com/questions/45504400/regex-match-pattern-of-alternating-characters
import re
def is_undulating(n):
  print(str(n))
  pattern = r'^([\d])(?!\1)([\d])(?:\1\2)*\1?$'
  if len(str(n)) < 3:
    return False
  return bool(re.search(pattern, str(n)))

