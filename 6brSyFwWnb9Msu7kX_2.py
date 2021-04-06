
def pos_neg_sort(l):
  pos = sorted( n for n in l if n>0 )
  return [ pos.pop(0) if n>0 else n for n in l ]

