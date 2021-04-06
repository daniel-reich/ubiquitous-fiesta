
import re
def count_number(lst):
  return sum(1 for i in re.split(', |]|,|\[', str(lst)) if i.replace('.','').isdigit())

