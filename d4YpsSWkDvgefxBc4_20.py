
def over_twenty_one(cards):
  sum_card = 0
  for card in cards:
    if type(card) == int:
      sum_card += card
    elif card in ["J", "K", "Q"]:
      sum_card += 10
  if "A" in cards:
    if sum_card + 11 > 21:
      if sum_card + 1 <= 21:
        return False
      else:
        return True
  if sum_card > 21:
    return True
  else:
    return False

