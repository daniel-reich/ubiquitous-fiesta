
def shuffle_count(deck, c=0):
  if isinstance(deck, int):deck = list(range(deck))   
  beg, end = deck[:len(deck)//2], deck[len(deck)//2:]
  new = [row for sub in zip(beg, end) for row in sub]
  c += 1
  return c if new == sorted(new) else shuffle_count(new, c)

