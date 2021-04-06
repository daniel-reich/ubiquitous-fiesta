
def poker_hand_ranking(hand):
  number_dict = {}
  suit_dict = {}
  ordered_hand = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  
  for card in hand:
    if len(card) > 2:
      number = card[:-1]
      suit = card[-1]
    else:
      number = card[0]
      suit = card[-1]
      
    if number in number_dict.keys():
      number_dict[number] += 1
    else:
      number_dict[number] = 1
      
    if suit in suit_dict.keys():
      suit_dict[suit].append(number)
    else:
      suit_dict[suit] = [number]
​
  print(number_dict)
  print(suit_dict)
  
  # Royal Flush
  royal_flush = ['10', 'J', 'Q', 'K', 'A']
  for key, value in suit_dict.items():
    if len(value) == 5:
      royal = True
      for card in value:
        if card not in royal_flush:
          royal = False
          break
      if royal:
        return 'Royal Flush'
      
  # Straight Flush
  for key, value in suit_dict.items():
    if len(value) == 5:
      for count, card in enumerate(ordered_hand):
        if card in value:
          try:
            if ordered_hand[count + 1] in value and ordered_hand[count + 2] in value and ordered_hand[count + 3] in value and ordered_hand[count + 4] in value:
              return 'Straight Flush'
          except:
            pass
​
  # Four of a Kind
  for key, value in number_dict.items():
    if number_dict[key] == 4:
      return 'Four of a Kind'
      
  # Full House
  two, three = False, False
  for key, value in number_dict.items():
    if number_dict[key] == 2:
      two = True
    elif number_dict[key] == 3:
      three = True
    if two and three:
      return 'Full House'
      
  # Flush
    for key, value in suit_dict.items():
      if len(value) == 5:
        return 'Flush'
  
  # Straight
  for count, card in enumerate(ordered_hand):
    if card in number_dict.keys():
      try:
        if ordered_hand[count + 1] in number_dict.keys() and ordered_hand[count + 2] in number_dict.keys() and ordered_hand[count + 3] in number_dict.keys() and ordered_hand[count + 4] in number_dict.keys():
              return 'Straight'
      except:
        pass
  
  # Three of a Kind
  if three:
    return 'Three of a Kind'
​
  # Two Pair
  pair = 0
  for key, value in number_dict.items():
    if number_dict[key] == 2:
      pair += 1
    if pair == 2:
      return 'Two Pair'
​
  # Pair
  if pair == 1:
      return 'Pair'
        
  # High Card
  return 'High Card'

