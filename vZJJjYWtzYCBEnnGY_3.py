
def briscola_score(my_deck1, my_deck2):
  score1 = 0
  score2 = 0
  for i in my_deck1:
    if i[0] == 'A':
      score1 += 11
    elif i[0] == '3':
      score1 += 10
    elif i[0] == 'K':
      score1 += 4
    elif i[0] == 'Q':
      score1 += 3
    elif i[0] == 'J':
      score1 += 2
    else:
      score1 += 0
​
  for i in my_deck2:
    if i[0] == 'A':
      score2 += 11
    elif i[0] == '3':
      score2 += 10
    elif i[0] == 'K':
      score2 += 4
    elif i[0] == 'Q':
      score2 += 3
    elif i[0] == 'J':
      score2 += 2
    else:
      score2 += 0
  if score1 + score2 > 120:
    return 'You Win!'
  elif score1 + score2 == 120:
    return 'Draw!'
  elif score1 + score2 < 120:
    return 'You Lose!'

