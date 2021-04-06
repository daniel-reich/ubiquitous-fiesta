
def combine(lst):
  symbolCount = max(itm[1] for itm in lst) + 1
  out = {}
  for ins in lst:
    src, sym, dst = ins
    if src not in out:
      out[src] = [None] * symbolCount
    out[src][sym] = dst
  return out

