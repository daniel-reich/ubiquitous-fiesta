
def bonus(days):
  if days<=32:
    return 0
  total=0
  for days in range(33,days+1):
    if days>=33 and days<=40:
      total+=325
    elif days>=41 and days<=48:
      total+=550
    else:
      total+=600
  return total

