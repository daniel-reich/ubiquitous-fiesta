
import re
def is_long_pressed(original, typed):
  p=''
  for x in original:
    p+=x+'+'
  return set(original)==set(typed) and bool(re.search(p,typed))

