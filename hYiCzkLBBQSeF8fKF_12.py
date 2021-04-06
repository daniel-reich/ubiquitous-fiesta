
def count(deck):
  return sum([1 for i in deck if i in [2,3,4,5,6]]) + sum([-1 for i in deck if i in [10, 'J', 'Q', 'K', 'A']])

