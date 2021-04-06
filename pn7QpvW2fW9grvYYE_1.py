
def find_fulcrum(lst):
  ls, rs = 0, sum(lst)
  for n in lst:
    rs -= n
    if ls == rs: return n
    ls += n
  return -1

