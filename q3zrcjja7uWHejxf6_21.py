
import re
def negative_sum(chars):
  return sum(int(a) for a in re.findall(r'-[0-9]+', chars))

