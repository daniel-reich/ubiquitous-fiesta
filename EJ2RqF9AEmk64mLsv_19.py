
def lottery(ticket, win):
  w = 0
  for i in ticket:
    for j in i[0]:
      if ord(j) == i[1]:
        w += 1
  if w >= win:
    return "Winner!"
  return "Loser!"

