
def is_ord_sub(smlst, biglst):
  i = 0
  for each in smlst:
    try:
      i = biglst.index(each,i) + 1
    except:
      return False
  return True

