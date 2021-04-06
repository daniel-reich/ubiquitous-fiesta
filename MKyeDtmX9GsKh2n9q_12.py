
def gen_deck():
    deck = []
    suits = ["d","h","c","s"]
    rank = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    for a in suits:
        for b in rank:
            deck.append(tuple([b,a]))
    return(deck)

