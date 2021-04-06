
import re
def validate_email(txt):
  if re.match("[^@]+@[^@]+\.[^@]+", txt):
    return True
  else:
    return False

