
import textwrap
def is_equal(lst):
  return sum([int(i) for i in textwrap.wrap(str(lst[0]),1)])==sum([int(j) for j in textwrap.wrap(str(lst[1]),1)])

