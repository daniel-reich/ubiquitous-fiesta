
def complete_binary(s):
  import math
  if len(s) % 8 == 0:
    return s
  else:
    return '0'*(8-(len(s) % 8))+s

