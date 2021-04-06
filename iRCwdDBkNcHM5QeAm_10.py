
def card_hide(card):
  end=card[-4:]
  for i in range(len(card)-4):
    card=card.replace(card[i], '*')
  return card[:-4]+end

