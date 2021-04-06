
def is_ord_sub(smlst, biglst):
  i = -1
  for n in smlst:
    i += 1
    while i<len(biglst) and n != biglst[i]:
      i += 1
    if i == len(biglst):
      return False
  return True

