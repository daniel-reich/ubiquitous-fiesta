
import re
def get_filename(path):
  return re.split(r'/', path)[-1]

