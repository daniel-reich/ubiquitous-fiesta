
def interview(lst, tot):
  if tot > 120:
    return "disqualified"
  if len(lst) != 8:
    return "disqualified"
  limit = 5
  check = 0
  for i in lst:
    if i > limit:
      return "disqualified"
    else:
      check+=1
      if ( check%2 )== 0:
        limit+=5
  return "qualified"

