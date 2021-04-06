
import re
def in_box(lst):
  for i in range (1,len(lst)-1):
    if re.search('#.*\*.*#', lst[i]):
      return True
  return False

