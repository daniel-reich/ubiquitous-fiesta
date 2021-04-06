
from itertools import groupby
def look_and_say(start, n):
  def integer(lst,s,num):
    lst.append(s)
    string = str(s)
    groups = [list(g) for k, g in groupby(str(string))]
    if num == 1:
      return lst
    else:
      return integer(lst,int(''.join(list(map(lambda x: str(len(x)) + x[0],groups)))),num-1)
  return integer([],start,n)

