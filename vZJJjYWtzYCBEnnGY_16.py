
def briscola_score(my_deck1, my_deck2):
  
  
  # Going Through Round One (aka First Deck)
  
  My_Total = 0
  
  for x in my_deck1:
    if (str(x[0]) == "A"):
      My_Total += 11
    elif (str(x[0]) == "3"):
      My_Total += 10
    elif (str(x[0]) == "K"):
      My_Total += 4
    elif (str(x[0]) == "Q"):
      My_Total += 3
    elif (str(x[0]) == "J"):
      My_Total += 2
    else:
      My_Total += 0
  
  My_Round1_Score = My_Total
  Opponent_Round1_Score = 120 - My_Round1_Score
  
  # Going Through Round Two (aka Second Deck)
  
  My_Total = 0
  
  for x in my_deck2:
    if (str(x[0]) == "A"):
      My_Total += 11
    elif (str(x[0]) == "3"):
      My_Total += 10
    elif (str(x[0]) == "K"):
      My_Total += 4
    elif (str(x[0]) == "Q"):
      My_Total += 3
    elif (str(x[0]) == "J"):
      My_Total += 2
    else:
      My_Total += 0
  
  My_Round2_Score = My_Total
  Opponent_Round2_Score = 120 - My_Round2_Score
  
  # Establishing Statement to Return
  if (My_Round1_Score + My_Round2_Score > 120):
    return "You Win!"
  elif (My_Round1_Score + My_Round2_Score < 120):
    return "You Lose!"
  else:
    return "Draw!"

