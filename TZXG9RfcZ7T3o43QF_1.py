
import re
def same_length(txt):
  one = re.findall(r'[1]+', txt)
  zero = re.findall(r'[0]+', txt)
  return len(one)==len(zero) and all(len(i)==len(j) for i,j in zip(one, zero))

