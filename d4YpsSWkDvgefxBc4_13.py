
def over_twenty_one(cards):
  if sum(10 if isinstance(x, str) else x for x in cards) > 21:
    if 'A' in cards:
      return sum(1 if "A" in x else 10 if isinstance(x, str) else x for x in cards) > 21
  return sum(10 if isinstance(x, str) else x for x in cards) > 21

