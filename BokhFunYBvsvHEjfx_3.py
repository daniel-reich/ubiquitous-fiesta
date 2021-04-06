
import re
def seven_boom(lst):
  lst = map(str, lst)
  if re.search('7', ''.join(lst)):
    return 'Boom!'
  else:
    return "there is no 7 in the list"

