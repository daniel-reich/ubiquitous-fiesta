
import re
​
def count_lone_ones(n):
  return sum(i == '1' for i in re.split('[^1]', str(n)))

