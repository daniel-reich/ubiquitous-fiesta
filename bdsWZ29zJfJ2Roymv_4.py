
import re
​
def swap_two(txt):
  return re.sub(r'(\w{2})(\w{2})', r'\2\1', txt)

