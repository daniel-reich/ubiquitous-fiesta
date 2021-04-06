
def is_ord_sub(smlst, biglst):
  for x in smlst:
    if x in biglst:
      biglst = biglst[biglst.index(x)+1:]
    else:
      return False
  return True

