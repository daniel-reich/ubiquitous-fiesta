
import math
def complete_binary(s):
  return '0'*(8*(math.ceil(len(s)/8)) - len(s))+s

