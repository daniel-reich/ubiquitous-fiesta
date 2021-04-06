
import re
def negative_sum(chars):
  negs = re.findall(r'-\d+', chars)
  return sum(int(neg) for neg in negs)

