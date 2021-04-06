
def dice_score(throw):
  totalCount = 0
  if throw.count(1)>=3:
    totalCount += 1000
    totalCount += throw.count(5)*50
    additionalOneCount = throw.count(1) - 3
    totalCount += additionalOneCount*100
  elif throw.count(6) >= 3:
    totalCount += 600
    totalCount += throw.count(1)*100
    totalCount += throw.count(5)*50
  elif throw.count(5) >= 3:
   totalCount += 500
   additionalFiveCount = throw.count(5) - 3
   totalCount += additionalFiveCount*50
   totalCount += throw.count(1)*100
  elif throw.count(4) >= 3:
    totalCount += 400
    totalCount += throw.count(1)*100
    totalCount += throw.count(5)*50
  elif throw.count(3) >= 3:
    totalCount += 300
    totalCount += throw.count(1)*100
    totalCount += throw.count(5)*50
  elif throw.count(2) >= 3:
    totalCount += 200
    totalCount += throw.count(1)*100
    totalCount += throw.count(5)*50
    
  return totalCount

