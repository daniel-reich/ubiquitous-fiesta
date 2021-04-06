
def getVal(ch):
  if ch=="A": return 1
  if ch == "J" or ch == "Q" or ch == "K": return 10
  return ch
def over_twenty_one(cards):
  return sum(getVal(ch) for ch in cards) >21

