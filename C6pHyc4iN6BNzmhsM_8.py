
def poker_hand_ranking(hand):
  def _value_card(card):
    if card == "A":
      return 14
    if card == "K":
      return 13
    if card == "Q":
      return 12
    if card == "J":
      return 11
    return int(card)
  
  def _is_straight(cs):
    if cs[-1] - cs[0] == 4:
      return True
    if cs[-1] == 14 and cs[0] == 2 and cs[-2] == 5:
      return True
    return False
    
  def _value_suit(suit):
    if suit == "s":
      return 0
    if suit == "h":
      return 1
    if suit == "d":
      return 2
    return 3
  
  suits = [_value_suit(x[-1]) for x in hand]
  cards = sorted([_value_card(x[:-1]) for x in hand])
  same_suit = len(set(suits)) == 1
  is_straight = _is_straight(cards)
  
  if same_suit and is_straight:
    if cards[0] == 10:
      return "Royal Flush"
    return "Straight Flush"
  
  num_cards = len(set(cards))
  
  if num_cards == 2:
    if cards[0] == cards[3] or cards[1] == cards[4]:
      return "Four of a Kind"
    return "Full House"
  
  if same_suit:
    return "Flush"
  
  if is_straight:
    return "Straight"
  
  for i in range(len(cards) - 2):
    if cards[i] == cards[i + 1] == cards[i + 2]:
      return "Three of a Kind"
  
  pairs = 0
  for i in range(len(cards) - 1):
    if cards[i] == cards[i + 1]:
      pairs += 1
  
  if pairs == 2:
    return "Two Pair"
  elif pairs == 1:
    return "Pair"
  
  return "High Card"

