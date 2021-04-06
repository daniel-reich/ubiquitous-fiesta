
import re
​
def validate_email(string):
  return bool(re.search(r'.+\@.+\.', string))

