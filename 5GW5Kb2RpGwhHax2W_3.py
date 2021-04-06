
def spiral_transposition(lst,res=None):
  if res is None:
    res = []
​
  res += lst.pop(0)
  if len(lst) == 0:
    return res
  else:
    lst = list(map(list, zip(*lst)))[::-1]
    return spiral_transposition(lst,res)

