
import re
​
def remove_abc(txt):
  if any(i in txt for i in ['a', 'b', 'c']):
    return re.sub('[abc]', '', txt) 
  else:
    return None

