
def briscola_score(my_deck1, my_deck2):
    d = {'A':11,'3':10,'K':4,'Q':3,'J':2}
    score1,score2 = sum(d.get(i[0],0) for i in my_deck1),sum(d.get(i[0],0) for i in my_deck2)
    if 120-score1 == score2: return 'Draw!'
    return 'You Win!' if 120-score1 < score2 else 'You Lose!'

