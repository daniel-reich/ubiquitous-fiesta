
import re
​
def first_place(road):
  c = re.findall(r'[a-z A-Z]', road)
  return None if not c else c[-1]

