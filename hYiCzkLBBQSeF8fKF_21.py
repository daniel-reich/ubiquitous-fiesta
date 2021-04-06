
def count(deck):
  r = 0
  for i in deck :
    if i in [2, 3, 4, 5, 6] :
      r += 1
    elif i in [10, 'J', 'Q', 'K', 'A'] :
      r -= 1
  return r

