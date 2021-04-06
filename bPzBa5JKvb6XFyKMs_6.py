
def get_primiera_score(deck):
    d = {'7':21, '6':18, 'A':16,
         '2':12, '3':13, '4':14, '5':15,
         'J':10, 'Q':10, 'K':10}
    hand = {'c': 0, 'd': 0, 'h': 0, 's': 0}
    for c, s in deck:
        hand[s] = max(hand[s],d[c])
    lov = list(hand.values())
    if 0 in lov:
        return 0
    return sum(lov)

