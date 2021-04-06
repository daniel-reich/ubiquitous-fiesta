
import math
def pages_in_book(total):
  return ((1 + math.sqrt(1-8*(-total)))/2).is_integer()

