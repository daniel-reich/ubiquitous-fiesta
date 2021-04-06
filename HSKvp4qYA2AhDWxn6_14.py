
def total_points(guesses, word):
  score = 0
  for guess in guesses:
    if all(guess.count(c) <= word.count(c) for c in set(guess)):
      score += len(guess) - 2
      if len(guess) == 6:
        score += 50
  return score

