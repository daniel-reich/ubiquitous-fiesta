
import re
def count_ones(lst):
  string = re.sub(r',|\s|[|]', '', str(lst))
  return len(re.findall(r'1(1)+', string))

