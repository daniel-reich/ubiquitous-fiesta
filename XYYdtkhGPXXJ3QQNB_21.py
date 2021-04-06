
def num_in_str(lst):
  import re
  return [x for x in lst if bool(re.match('^(?=.*[0-9])', x))]

