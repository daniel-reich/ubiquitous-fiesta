
import string
def how_many_times(msg):
  dicto = {}
  total = 0 
  num = 0
  asc = list(list(string.ascii_lowercase))
  for x in range(1,27):
    dicto[asc[num]] = x
    num += 1 
  for a in msg:
    total += dicto[a]
  return total

