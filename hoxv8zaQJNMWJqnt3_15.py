
import math
def is_heteromecic(n):
  return n == int(math.sqrt(n))*(int(math.sqrt(n))+1) or n == (int(math.sqrt(n))+1)*(int(math.sqrt(n))+2)

