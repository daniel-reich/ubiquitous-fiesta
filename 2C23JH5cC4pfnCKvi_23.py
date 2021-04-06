
def check_flush(table, hand):
    Spades = []
    Hearts = []
    Diamonds = []
    Clubs = []
    table.append(cards for cards in hand)
    for cards in table:
        for card in cards:
            if card[-1] == "S":
                Spades.append(card)
            if card[-1] == "H":
                Hearts.append(card)
            if card[-1] == "D":
                Diamonds.append(card)
            if card[-1] == "C":
                Clubs.append(card)
                
    if len(Spades) >= 5 or len(Hearts) >= 5 or len(Diamonds) >= 5 or len(Clubs) >= 5:
        return True
    else:
        return False

