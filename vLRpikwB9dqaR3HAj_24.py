
def is_ord_sub(smlst, biglst):
  smlst = smlst[::-1]
​
  for num in biglst:
    if(len(smlst) > 0 and num == smlst[-1]):
      smlst.pop()
​
  return len(smlst) == 0

