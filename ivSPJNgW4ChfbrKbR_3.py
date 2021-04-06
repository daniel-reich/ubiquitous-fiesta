
def soroban(soroban):
  temp = 0
  top_deck = ""
  lower_deck = ""
  for i in soroban[0]:
    for each in i:
      if each == "O":
        top_deck += "0"
      else:
        top_deck += "5"
        
  for x in range(7):
    for i in range(3,8):
      if soroban[i][x] == "|" and i == 3:
        lower_deck += "0"
        break
      if soroban[i][x] == "O":
        temp += 1
      elif soroban[i][x] == "|":
        lower_deck += str(temp)
        temp = 0
        break
        
        
  return (int(lower_deck) + int(top_deck))

