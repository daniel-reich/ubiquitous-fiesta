
def briscola_score(my_deck1, my_deck2):
  d = {"A":11,"3":10,"J":2,"Q":3,"K":4}
  myscore = sum(d[i[0]] for i in my_deck1+my_deck2 if i[0] in "A3JQK")
  return "You Lose!" if myscore<120 else "You Win!" if myscore>120 else "Draw!"

