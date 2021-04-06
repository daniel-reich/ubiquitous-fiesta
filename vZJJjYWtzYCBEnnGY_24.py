
def briscola_score(my_deck1, my_deck2):
  
  A = 11
  three = 10
  K = 4
  Q = 3
  J = 2
  
  to_win = 120
  
  deck1_points = 0
​
  for card in my_deck1:
    card = list(card)
    try:
      i = int(card[0])
      if i == 3:
        deck1_points += three
    except ValueError:
      deck1_points += eval(card[0])
  
  deck2_necessary = to_win - deck1_points
  deck2_points = 0
  
  for card in my_deck2:
    card = list(card)
    try:
      i = int(card[0])
      if i == 3:
        deck2_points += three
    except ValueError:
      deck2_points += eval(card[0])
  
  if deck2_necessary == deck2_points:
    return "Draw!"
  elif deck2_points > deck2_necessary:
    return 'You Win!'
  else:
    return 'You Lose!'

