
def over_twenty_one(cards):
  value = 0
  for i in cards:
    if type(i) == int:
      value += i
    elif i in "JKQ":
      value += 10
    elif i == "A" and value + 11 <= 21:
      value += 11
    else: 
      value += 1
  if value > 21 and "A" in cards:
    value -= 10
  return value > 21

