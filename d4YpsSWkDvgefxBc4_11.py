
def over_twenty_one(cards):
  total = 0
  face = 'JQK'
  for card in cards:
    if str(card) in face:
      total += 10
    elif card == 'A':
      total += 1
    else:
      total += card
  return total > 21

