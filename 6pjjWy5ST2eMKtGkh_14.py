
import re
def replace(txt, r):
  return re.sub('['+r+']','#',txt)

