
import re
​
def count_ones(lst):
  return len(re.split("1(?:, 1)+", str(lst))) - 1

