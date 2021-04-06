
import re
def negative_sum(chars):
  p=re.compile('\-?\d+')
  return sum([int(x) for x in p.findall(chars) if int(x)<0])

