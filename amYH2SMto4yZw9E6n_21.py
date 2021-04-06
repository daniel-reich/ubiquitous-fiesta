
import re
​
def validate(s):
  return bool(re.match(r'^\+?1?\s?[/\-.(]?\s?[0-9]{3}[/\-.)]?\s?[0-9]{3}[/\-.]?\s?[0-9]{4}$',s))

