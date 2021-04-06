
import re
def num_args(func):
  try:func();return 0
  except Exception as e:
    return int(re.search(r'\d+',str(e)).group(0))

