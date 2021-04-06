
import re
​
​
def validate_email(txt):
​
  pattern = '\w+\.?\w+@\w+\.\w+'
  return bool(re.match(pattern, txt))

