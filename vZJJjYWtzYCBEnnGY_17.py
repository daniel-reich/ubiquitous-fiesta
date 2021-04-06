
def briscola_score(my_deck1, my_deck2):
  total1 = 0 
  total2 = 0
  for card in my_deck1:
    if card[0] == 'A':
      total1 += 11 
    elif card[0] == '3':
      total1 += 10 
    elif card[0] == 'K':
      total1 += 4 
    elif card[0] == 'Q':
      total1 += 3 
    elif card[0] == 'J':
      total1 += 2
​
  for card in my_deck2:
    if card[0] == 'A':
      total2 += 11 
    elif card[0] == '3':
      total2 += 10 
    elif card[0] == 'K':
      total2 += 4 
    elif card[0] == 'Q':
      total2 += 3 
    elif card[0] == 'J':
      total2 += 2
​
  if total1 + total2 == 120:
    return "Draw!"
  if total2 < (121 - total1):
    return "You Lose!"
  else:
    return "You Win!"

