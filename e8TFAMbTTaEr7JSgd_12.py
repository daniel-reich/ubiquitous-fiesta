
import re
def left_digit(num):
  return int(re.search(r"\d", num).group())

