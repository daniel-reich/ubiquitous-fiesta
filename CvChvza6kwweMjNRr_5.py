
import re
​
def split_code(item):
  letters, numbers = re.findall(r'[A-Z]+|\d+', item)
  return [letters, int(numbers)]

