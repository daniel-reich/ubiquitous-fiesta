
from itertools import*
def look_and_say(s,n):
  r=[s]
  while len(r)<n:
    s=int(''.join(str(len(list(v)))+k for k,v in groupby(str(s))))
    r.append(s)
  return r

