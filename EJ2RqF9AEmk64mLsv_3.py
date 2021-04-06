
def lottery(ticket, win):
  count=0
  for i in ticket:
    a=False
    for j in i[0]:
      if ord(j)==i[1]:a=True
    if a:count+=1
  return 'Winner!' if count>=win else "Loser!"

