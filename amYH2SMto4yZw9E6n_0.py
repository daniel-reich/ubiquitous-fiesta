
import re
​
def validate(s):
  return bool(re.match(r'(\+1|1)?[ /.-]?\(?\d{3}\)?[ /.-]?\d{3}[ /.-]?\d{4}$', s))

