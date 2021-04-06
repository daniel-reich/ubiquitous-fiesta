
import re
def camel_to_snake(s):
  return re.sub('([A-Z])', r'_\1', s).lower()

