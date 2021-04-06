
import re
​
def validate(s):
  ret = re.match(r'\+1?|1?[- ./]?\(?(\d{3})\)?[- ./]?(\d{3})[- ./]?(\d{4})$', s)
  return ret is not None

