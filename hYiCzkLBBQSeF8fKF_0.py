
def count(deck):
  return sum([1 if str(i) in '23456' else -1 if str(i) in 'AKQJ10' else 0 for i in deck])

