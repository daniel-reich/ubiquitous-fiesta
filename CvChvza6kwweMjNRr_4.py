
import re
​
def split_code(item):
  lst = re.split(r"(?=\d)(\w+)",item)
  return [lst[0],int(lst[1])]

