
import re
def longest_substring(digits):
  u = re.findall(r"(?:[13579][02468])+[13579]?|(?:[02468][13579])+[02468]?", digits)
  return [v for v in u if len(v) == max(map(len,u))][0]

