
import re
def replace_nums(string):
  return re.sub(r'(\d+)',lambda m:bin(int(m.group(1)))[2:],string)

