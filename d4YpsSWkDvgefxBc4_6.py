
def over_twenty_one(cards):
  v = 0
  for i in cards:
    if str(i) in "JQK":
      v = v + 10
    elif str(i) == 'A':
      v = v + 1
    else:
      v = v + i
  return v > 21

