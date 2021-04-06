
def is_ord_sub(smlst, biglst):
  for i in smlst:
    if i in biglst: biglst = biglst[biglst.index(i)+1:]
    else: return False
  return True

