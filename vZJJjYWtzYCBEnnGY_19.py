
def briscola_score(my_deck1, my_deck2):
  scores = { 'A': 11, '3': 10, 'K':4, 'Q':3, 'J': 2 }
  hand_value = lambda hnd: sum(scores[c[0]] for c in hnd if c[0] in 'AKQJ3')
  
  pts = hand_value(my_deck1) + hand_value(my_deck2)
  return "You Win!" if pts > 120 else "You Lose!" if pts < 120 else "Draw!"

