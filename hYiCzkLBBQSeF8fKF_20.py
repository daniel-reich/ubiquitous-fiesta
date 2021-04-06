
def count(deck):
  c = 0
  for i in deck:
    if i in [2,3,4,5,6]:
      c += 1
    elif i in [10,'J','Q','K','A']:
      c -= 1
  return c

