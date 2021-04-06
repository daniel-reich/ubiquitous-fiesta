
def mini_win_check(ticket):
  s,p=ticket
  for char in s:
    if ord(char)==p:
      return 1
  return 0
​
def lottery(ticket, win):
  return "Winner!" if sum(map(mini_win_check,ticket))>=win else "Loser!"

