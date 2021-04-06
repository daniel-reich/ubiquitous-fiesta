
def over_twenty_one(cards):
  sum = 0
  for i in range(len(cards)):
    if cards[i] == "J": cards[i] = 10
    if cards[i] == "Q": cards[i] = 10
    if cards[i] == "K": cards[i] = 10
    if cards[i] == "A": cards[i] = 1
  for j in range(len(cards)):
    sum += cards[j]
  if sum <= 21: return False
  else: return True

