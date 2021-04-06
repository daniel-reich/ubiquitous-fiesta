
import re
def is_there_consecutive(lst, n, times):
  if len(lst)==1 and lst[0]==n and times==0:
    return False
  else:
    s=''.join([str(x) for x in lst])
    return bool(re.search(str(n)*times, s))

