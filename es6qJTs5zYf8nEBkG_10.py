
import re
def is_rectangle(lst):
  if len(lst) != 4:
    return False
  num = []
  items = []
  for x in range(0, len(lst)):
    result = [int(d) for d in re.findall(r'-?\d+', lst[x])]
    num.extend(result)
  for x in range(0, len(num)):
    if num[x] not in items:
      items.append(num[x])
  if len(items) != 4:
    return False
  return True

