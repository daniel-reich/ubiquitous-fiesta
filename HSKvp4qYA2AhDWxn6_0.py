
def total_points(guesses, word):
  total = 0
  for g in guesses:
    if all(word.count(i)>=g.count(i) for i in g):
      total += len(g)-2
      if len(g)==6:
        total+=50
  return total

