
import re
​
def digit_count(num):
  num  = str(num)
  return int(re.sub(r"\d" , lambda m : str(num.count(m.group())) ,num))

