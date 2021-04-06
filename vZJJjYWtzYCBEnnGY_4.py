
def briscola_score(my_deck1, my_deck2):
    cards_rank = {'A': 11, '3': 10, 'K': 4, 'Q': 3, 'J': 2,
             '7': 0, '6': 0, '5': 0, '4': 0,
             '2': 0}
    total1, total2 = 0, 0
    for card in my_deck1:
        for i in card:
            if i.isdigit() or i.isupper():
                total1 += cards_rank[i]
    for card in my_deck2:
        for i in card:
            if i.isdigit() or i.isupper():
                total2 += cards_rank[i]
    if total2 < (120 - total1):
        return "You Lose!"
    elif total2 > (120 - total1):
        return "You Win!"
    else:
        return "Draw!"

