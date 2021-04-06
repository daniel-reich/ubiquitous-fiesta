
import re
​
def validate_email(txt):
  return bool(re.search(r'\w+@\w+\.\w+', txt))

