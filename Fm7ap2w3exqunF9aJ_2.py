
import re
​
def count_lone_ones(n):
  return re.sub("11+", "", str(n)).count("1")

