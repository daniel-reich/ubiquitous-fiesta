
def canConcatenate(lst, target):
  nlst = []
  for  sub in lst:
    for i in sub:
      nlst.append(i)
  return sorted(nlst)==sorted(target)

