
values = {'7': 21, '6':18, 'A':16, '2':12, '3':13, '4':14, '5':15, 'J':10, 'Q':10, 'K':10}
​
def get_primiera_score(deck):
  hearts = []
  clubs = []
  diamonds = []
  spades = []
  for i in deck:
    if i[1] == 'h':
      hearts.append(values[i[0]])
    elif i[1] == 'c':
      clubs.append(values[i[0]])
    elif i[1] == 'd':
      diamonds.append(values[i[0]])
    else:
      spades.append(values[i[0]])
  if len(hearts) == 0 or len(clubs) == 0 or len(diamonds) == 0 or len(spades) == 0:
    return 0
  return max(hearts) + max(clubs) + max(diamonds) + max(spades)

