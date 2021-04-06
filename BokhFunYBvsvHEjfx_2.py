
import re
def seven_boom(lst):
  new_list = []
  for number in lst:
      new_list.append(str(number))
  new_list = "".join(new_list)
  pattern = re.findall(r'7', new_list)
  if "7" in pattern:
    return "Boom!"
  else:
    return "there is no 7 in the list"

