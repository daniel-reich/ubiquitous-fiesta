
import re
​
​
def to_camel_case(txt):
  lst = re.split(r'[-_]', txt)
  return lst[0] + ''.join(i.title() for i in lst[1:])

