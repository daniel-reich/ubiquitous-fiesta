
import re
​
​
def swap_xy(txt):
  numbers = re.findall('-?\d+', txt)
  return '({}, {}), ({}, {})'.format(
    numbers[1], numbers[0], numbers[3], numbers[2]
  )

