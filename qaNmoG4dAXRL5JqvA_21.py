
def sum_fractions(lst):
  fracLst = []
  total = 0
  for nlst in lst:
    curFrac = nlst[0] / nlst[1]
    fracLst.append(curFrac)
  for frac in fracLst:
    total = frac + total
  return round(total)

