
import re
​
def comments_correct(txt):
  return not re.sub(r'[/]{2}|/\*\*/', '', txt)

