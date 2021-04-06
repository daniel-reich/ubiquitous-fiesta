
def determine_who_cursed_the_most(d):
  
  My_Swearing_Numbers = []
  Spouse_Swearing_Numbers = []
  
  Counter = 0
  Length = len(d)
  
  Item = d["round1"]
  My_Swearing_Numbers.append(Item["me"])
  Spouse_Swearing_Numbers.append(Item["spouse"])
  
  Item = d["round2"]
  My_Swearing_Numbers.append(Item["me"])
  Spouse_Swearing_Numbers.append(Item["spouse"])
  
  Item = d["round3"]
  My_Swearing_Numbers.append(Item["me"])
  Spouse_Swearing_Numbers.append(Item["spouse"])
    
  My_Total = 0
  
  for x in My_Swearing_Numbers:
    My_Total += x
  
  Spouse_Total = 0
  
  for x in Spouse_Swearing_Numbers:
    Spouse_Total += x
  
  if (My_Total > Spouse_Total):
    return "ME!"
  elif (Spouse_Total > My_Total):
    return "SPOUSE!"
  else:
    return "DRAW!"

