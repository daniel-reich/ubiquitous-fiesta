
def card_hide(card):
    card = str(card)
    return "*" * (len(card) - 4) + card[len(card) - 4: len(card)]

