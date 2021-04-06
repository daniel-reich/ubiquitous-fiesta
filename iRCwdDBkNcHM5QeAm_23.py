
def card_hide(card):
  a = len(card)
  x = card[-4:]
  y = '*'
  return str(y * (a - 4) + x)

