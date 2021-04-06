
import re
​
def grab_number_sum(s):
  numbers = re.findall(r"\d+", s)
  return sum(int(num) for num in numbers)

