
def bill_split(spicy, cost):
  a=len(spicy)
  newLst=[]
  sSum=0
  nsSum=0
  for i in range(0,a):
    if(spicy[i]=="S"):
      sSum=sSum+cost[i]
    else:
      sSum=sSum+(cost[i]/2)
      nsSum=nsSum+(cost[i]/2)
  newLst.append(sSum)
  newLst.append(nsSum)
  return newLst

