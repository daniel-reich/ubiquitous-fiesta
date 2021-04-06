
def lottery(ticket, win):
  count = 0
  for row in ticket:
    ch = chr(row[1])
    for char in row[0]:
      if char == ch:
        count += 1
        break
  return "Winner!" if count >= win else "Loser!"

