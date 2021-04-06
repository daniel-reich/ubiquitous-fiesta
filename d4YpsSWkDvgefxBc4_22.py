
def over_twenty_one(cards):
  Vals = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10, "A":11}
  total = sum([Vals[i] for i in cards])
  if "A" in cards and total> 12:
    total -= 10
  return total > 21

