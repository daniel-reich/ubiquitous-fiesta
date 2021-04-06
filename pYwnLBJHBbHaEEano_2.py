
import re
def hash_plus_count(txt):
  return [len(re.findall(r"\#",txt)), len(re.findall(r"\+",txt))]

