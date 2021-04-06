
def briscola_score(my_deck1, my_deck2):
    cards = {"A":11,"3":10,"K":4,"Q":3,"J":2}
    round1 = sum(cards[card[0]] for card in my_deck1 if card[0] in cards)
    round2 = sum(cards[card[0]] for card in my_deck2 if card[0] in cards)
    goal = 120 - (round1 + 1)
    if round1+round2 == 120: return "Draw!"
    elif round2 >= goal: return "You Win!"
    else: return "You Lose!"

