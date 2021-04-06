
def briscola_score(deck1, deck2):
  d = {"A":11, "3":10, "K":4, "Q":3, "J":2}
  def pts(deck):
    de = [x[0] for x in deck]
    return sum(d[i] for i in de if i in d.keys())
  r = pts(deck1) + pts(deck2)
  return "You Win!" if r>120 else "You Lose!" if r<120 else "Draw!"

