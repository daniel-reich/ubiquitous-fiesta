
def count(deck):
  
  one = [2, 3, 4, 5, 6]
  zero = [7, 8, 9]
  neg_one = [10, 'J', 'Q', 'K', 'A']
  
  result = 0
  
  for card in deck:
    
    if card in one:
      result += 1
    elif card in zero:
      result += 0
    elif card in neg_one:
      result += -1
    else:
      return 'Error!'.upper() + '{}Incorrect card value'.format(card)
  
  return result

