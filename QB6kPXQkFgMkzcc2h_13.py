
import re
​
def remove_abc(txt):
  p = re.sub('[abc]','',txt)
  return p if p != txt else None

