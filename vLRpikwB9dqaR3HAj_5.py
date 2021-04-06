
def is_ord_sub(smlst, biglst):
  for i,n in enumerate(smlst):
    if n in biglst:
      if i==len(smlst)-1:
        return True
      idx = biglst.index(n)
      if len(biglst)>1:
        biglst=biglst[idx+1:]
      else:
        return True
    else:
      return False

