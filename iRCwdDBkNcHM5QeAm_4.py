
def card_hide(card):
  #Write a function that takes a credit card number and only displays the last four character
  #The rest of the card number must be replaced by ************
  result = ''
  for c in range(len(card) - 4):
    result += '*'
  return result + card[-4:]

