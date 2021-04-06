
def interview(lst, tot):
  mins = {0:5,1:5,2:10,3:10,4:15,5:15,6:20,7:20}
  maxTime = 0
  for i in range(0,len(lst)):
    maxTime += mins[i]
    if lst[i] > mins[i]:
      return "disqualified"
  if tot <= maxTime + 20:
    print(tot,maxTime+20)
    return "qualified"
  else:
    print(tot,maxTime+20)
    return "disqualified"

