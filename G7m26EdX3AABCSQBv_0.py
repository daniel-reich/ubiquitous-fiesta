
import re
​
def format_ascii(txt, width):
  return '\n'.join(re.findall('.'*width, txt))

