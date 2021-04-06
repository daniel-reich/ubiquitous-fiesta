
from itertools import takewhile
def numbers_to_ranges(lst):
  def ranges(newlst,lst):
    if not lst:
      return newlst
    else:
      lst2 = list(takewhile(lambda x: x[0] == x[1], zip(lst,list(range(lst[0],len(lst) + lst[0])))))
      lower = lst2[0][0]
      higher = lst2[-1][0]
      if lower == higher:
        newlst.append(str(lower))
      else:
        newlst.append("{}-{}".format(str(lower),str(higher)))
      return newlst if lst[-1] == higher else ranges(newlst,lst[lst.index(higher)+1::])
  return ranges([],lst)

