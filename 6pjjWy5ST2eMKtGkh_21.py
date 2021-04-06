
import re
def replace(txt, r):
  return re.sub('[{}]'.format(r), 
                 '#', txt)

