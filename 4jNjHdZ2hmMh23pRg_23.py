
def cutting_grass(lst, *cuts):
  n = []
  for cut in cuts:
    nlst = n[-1] if n else lst
    cn = []
    for bl in nlst:
      try:
        bl - cut
      except TypeError:
        cn = 'Done'
        break
      else:
        if not bl - cut: 
          cn = 'Done'
          break
        else:
          cn.append(bl - cut)
    n.append(cn)
  return n

