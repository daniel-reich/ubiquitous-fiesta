
def interview(lst, tot):
  key=[5, 5, 10, 10, 15, 15, 20, 20]
  if tot>120 or len(lst)<8:
    return "disqualified"
  while len(lst)>0:
    if lst.pop()>key.pop():
      return "disqualified"
  return "qualified"

