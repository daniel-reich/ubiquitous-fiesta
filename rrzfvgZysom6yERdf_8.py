
def player1_wins(lst):
  return sum(score(e[:14])>score(e[15:]) for e in lst)
​
types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
​
def score(cards):
    return sorted([(cards.count(types[i]), i) for i in range(13)])[::-1]

