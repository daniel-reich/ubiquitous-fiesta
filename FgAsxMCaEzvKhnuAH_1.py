
from re import findall
def deep_sum(r):
  return sum(int(x) for x in findall("-?\\d+", str(r)))

