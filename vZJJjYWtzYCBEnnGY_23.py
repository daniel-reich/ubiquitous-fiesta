
def briscola_score(my_deck1, my_deck2):
  count = 120
  points = {"A":11, "K":4, "Q":3, "J":2,"3":10}
  for i in my_deck1:
    if i[0] in points.keys():
      count -= points[i[0]]
  for j in my_deck2:
    if j[0] in points.keys():
      count -= points[j[0]]
  if count > 0:
    return "You Lose!"
  elif count == 0:
    return "Draw!"
  else:
    return "You Win!"

