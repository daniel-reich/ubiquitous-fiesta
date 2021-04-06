
def card_hide(card):
  return ''.join('*' for x in range(len(card)-4))+''.join(card[-4:])

