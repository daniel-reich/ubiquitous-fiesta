
import re
​
def validate_email(txt):
  if (re.match('[a-zA-Z0-9]+.?[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}',txt)):
    return True
  else: 
    return False

