
def calculate_score(games):
  Benson = 0
  Abigail = 0
  for i in games :
      if  i[0] == "R" and i[1] == "P" :
          Benson += 1
      elif i[0] == "R" and i[1] == "S" :
          Abigail += 1
      elif i[0] == "S" and i[1] == "P" :
          Abigail += 1
      elif i[0] == "S" and i[1] == "R" :
          Benson += 1
      elif i[0] == "P" and i[1] == "S" :
          Benson += 1
      elif i[0] == "P" and i[1] == "R" :
          Abigail += 1
          
  if Abigail > Benson :
    return "Abigail"
  elif Abigail < Benson :
    return "Benson"
  elif Abigail == Benson :
    return "Tie"

