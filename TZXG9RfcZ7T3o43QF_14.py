
import re
def same_length(txt):
  one = re.findall('1+', txt)
  zero = re.findall('0+', txt)
  return all(len(o) == len(z) for o, z in zip(one, zero)) and len(one) == len(zero)

