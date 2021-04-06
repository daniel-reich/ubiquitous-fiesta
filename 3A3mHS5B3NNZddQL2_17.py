
def interview(lst, tot):
  mx = 5
  for i,j in zip(lst[1::2],lst[::2]):
    if i > mx or j > mx:
      return "disqualified"
    mx+=5
  if tot > 120:
    return "disqualified"
  if len(lst) != 8:
    return "disqualified"
  return "qualified"

