
import re
def construct_fence(p):
  p = re.sub(r'\D+','',p)
  return "H" * (1000000 // int(p))

