
def count(deck):
  BlackJack = {
    "J" : -1, 
    "Q" : -1,
    "K" : -1, 
    "A" : -1
  }
  
  newArr = []
  
  for i in deck:
    if i in BlackJack:
      newArr.append(BlackJack[i])
    else:
      if i <= 6:
        newArr.append(1)
      elif i > 6 and i <= 9:
        newArr.append(0)
      elif i == 10:
        newArr.append(-1)
        
  return sum(newArr)

