
def ranged_reversal(lst, st, fi):
  if st == 0:
    return lst[fi::-1] + lst[fi+1:]
  else:
    return lst[:st] + lst[fi:st-1:-1] + lst[fi+1:]

