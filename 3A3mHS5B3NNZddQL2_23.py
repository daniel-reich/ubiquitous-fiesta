
def interview(lst, tot):
  max_time = [5,5,10,10,15,15,20,20]
  if len(lst)==8:
    if tot>120:
      return "disqualified"
    else:
      for i in range(len(lst)):
        if lst[i]>max_time[i]:
          return "disqualified"
          break
      else:
        return "qualified"
  else:
    return "disqualified"

