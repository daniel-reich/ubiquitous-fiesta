
points = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, '3': 10, '2': 0}
points.update(dict((str(k), 0) for k in range(4, 8)))
​
def briscola_score(my_deck1, my_deck2):
  myscore = sum(points[card[0]] for card in my_deck1 + my_deck2)
  return 'Draw!' if myscore == 120 else ('You Win!' if myscore > 120 else 'You Lose!')

