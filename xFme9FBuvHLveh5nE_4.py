
import re
​
def is_zygodrome(num):
  return not re.sub(r"(\d)\1+", "", str(num))

