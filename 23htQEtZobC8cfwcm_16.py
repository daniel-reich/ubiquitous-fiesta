
def canConcatenate(lst, target):
  nlst = []
  for el in lst:
    nlst += el
  nlst.sort()
  target.sort()
  return nlst == target

