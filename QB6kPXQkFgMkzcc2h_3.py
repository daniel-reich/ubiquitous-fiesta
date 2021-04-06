
import re
def remove_abc(txt):
  t = re.sub(r'[abc]','',txt)
  return None if t == txt else t

