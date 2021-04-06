
def briscola_score(my_deck1, my_deck2):
  my_score1 = 0
  my_score2 = 0
  scored_cards = ['A', '3', 'K', 'Q', 'J']
  for i in my_deck1:
    if i[0] == scored_cards[0]: my_score1 += 11
    elif i[0] == scored_cards[1]: my_score1 += 10
    elif i[0] == scored_cards[2]: my_score1 += 4
    elif i[0] == scored_cards[3]: my_score1 += 3
    elif i[0] == scored_cards[4]: my_score1 += 2
  opponent_score = 120 - my_score1
  for i in my_deck2:
    if i[0] == scored_cards[0]: my_score2 += 11
    elif i[0] == scored_cards[1]: my_score2 += 10
    elif i[0] == scored_cards[2]: my_score2 += 4
    elif i[0] == scored_cards[3]: my_score2 += 3
    elif i[0] == scored_cards[4]: my_score2 += 2
​
  if (my_score2 >= (opponent_score + 1)): return("You Win!")
  elif (my_score2 <= (opponent_score - 1)): return("You Lose!")
  else: return("Draw!")

