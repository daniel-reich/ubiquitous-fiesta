
import re
def find_vertex(x):
  a, b, c = (int(n) for n in re.findall(r'-?\d+', x))
  return -b // (2 * a)

