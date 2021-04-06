
def award_prizes(names):
  namesLst = sorted(names.items(),key=lambda x: x[1],reverse=True)
  res = {}
  for i,n in enumerate(namesLst):
    if i == 0:
      res[n[0]] = 'Gold'
    elif i == 1:
      res[n[0]] = 'Silver'
    elif i == 2:
      res[n[0]] = 'Bronze'
    else:
      res[n[0]] = 'Participation'
  return res

