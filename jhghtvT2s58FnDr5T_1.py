
import re
​
def jazzify(lst):
  return [re.sub('(?<!7)$', '7', i) for i in lst]

