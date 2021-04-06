
import math
def num_of_digits(num):
  return 1 if num ==0 else int(math.log10(abs(num)))+1

