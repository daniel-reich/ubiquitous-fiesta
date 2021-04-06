
def is_ord_sub(smlst, biglst):
  if not smlst: return True
  if not smlst[0] in biglst: return False
  r = biglst.index(smlst[0])
  return is_ord_sub(smlst[1:], biglst[r+1:])

