
def is_ord_sub(smlst, biglst):
  smlst.reverse()
  i = 0
  while smlst and i < len(biglst):
    if biglst[i] == smlst[-1]:
      smlst.pop()
    i += 1
  return not(smlst)

