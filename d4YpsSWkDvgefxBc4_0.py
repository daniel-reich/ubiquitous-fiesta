
value = {'A':1,'J':10,'Q':10,'K':10}
def over_twenty_one(cards):
  return sum(c if str(c).isdigit() else value[c] for c in cards) > 21

