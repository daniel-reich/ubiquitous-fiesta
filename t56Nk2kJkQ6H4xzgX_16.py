
import re
def swap_xy(txt):
  numbers = [int(d) for d in re.findall(r'-?\d+', txt)]
  
  return "({}, {}), ({}, {})".format(numbers[1], numbers[0], numbers[3], numbers[2])

