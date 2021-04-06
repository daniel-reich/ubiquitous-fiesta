
import re
def remove_abc(t):
  s=re.sub('[abc]','',t)
  return None if s==t else s

