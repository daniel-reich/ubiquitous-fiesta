
def check_flush(table, hand):
  def table_check(t):
    suits = []
​
    for card in table:
      c = card.split('_')
      num = c[0]
      suit = c[1]
​
      suits.append(suit)
    
    pos = False
    imp_suit = None
​
    for suit in suits:
      c = suits.count(suit)
      if c >= 3:
        pos = True
        imp_suit = suit
        break
    
    return [pos, imp_suit]
  def hand_check(h):
    suits = []
    for card in h:
      c = card.split('_')
      num = c[0]
      suit = c[1]
​
      suits.append(suit)
    
    c = suits.count(suits[0])
​
    if c == 2:
      return [True, suits[0]]
    else:
      return False
  
  tc = table_check(table)
  if tc == False:
    return False
  hc = hand_check(hand)
  if hc == False:
    return False
  else:
    table_suit = tc[1]
    hand_suit = hc[1]
    
    if table_suit == hand_suit:
      return True
    else:
      return False

