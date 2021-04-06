
import math
def group(lst, size):
  step = math.ceil(lst[-1] / size)
  return [lst[i::step] for i in range(step)]

