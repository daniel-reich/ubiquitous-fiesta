
import re
​
def swap_two(string):
  return re.sub(r"([\s\S][\s\S])([\s\S][\s\S])" , lambda m : m.group(2)+m.group(1), string);

