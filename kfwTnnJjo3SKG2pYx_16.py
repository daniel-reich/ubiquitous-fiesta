
import re
​
def replace_nums(txt):
  return re.sub('\d+', lambda x: bin(int(x.group(0)))[2:], txt)

