
def over_twenty_one(cards):        
    cards = [10 if isinstance(x, str) and x in 'JQK' else x for x in cards]
    if 'A' in cards:
        return sum(cards[: cards.index('A')]+ cards[cards.index('A')+1: ])>=21
    else:
        return sum(cards)>21

