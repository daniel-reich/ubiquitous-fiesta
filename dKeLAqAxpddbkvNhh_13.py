
import re
​
def group_seats(lst, n):
  return sum(sum(max(0, 1+j-n) for j in map(len, re.findall('0+', ''.join(map(str, i))))) for i in lst)

