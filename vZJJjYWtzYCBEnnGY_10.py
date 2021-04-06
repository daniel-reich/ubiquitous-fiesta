
def briscola_score(my_deck1, my_deck2):
  d=dict(zip("A3KQJ",[11,10,4,3,2]))
  def score(n):
    return d[n[0]] if n[0] in "A3KQJ" else 0
​
  t=sum(map(score,my_deck1+my_deck2))
  if t==120:
    return "Draw!"
  else: 
    return "You {}!".format(['Lose','Win'][t>120])

