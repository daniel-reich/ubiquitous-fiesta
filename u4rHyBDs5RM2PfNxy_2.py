
import re
​
def count_ones(A):
  return len(re.findall('1(, 1)+', '%s' % A))

