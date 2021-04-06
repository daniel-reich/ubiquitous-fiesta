
import re
def camelCasing(txt):
  if len(txt) == 0:
    return txt
  lst = re.split("[_\s]", txt)
  result = lst[0].lower()
  for word in lst[1:]:
    result += word.title()
  return result

