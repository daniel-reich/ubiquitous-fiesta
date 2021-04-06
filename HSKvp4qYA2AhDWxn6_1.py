
def total_points(guesses, word):
  points = 0
  for guess in guesses:
    if all(guess.count(ch) <= word.count(ch) for ch in guess):
      points += len(guess) -2 if len(guess) < 6 else 54
​
  return points

