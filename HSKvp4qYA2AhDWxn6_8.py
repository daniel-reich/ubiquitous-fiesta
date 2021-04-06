
def total_points(guesses, word):
  def score_guess(guess):
    for key,val in ({c:guess.count(c) for c in guess}).items():
      if word.count(key) < val: return 0
    return 1 if len(guess) == 3 else 2 if len(guess) == 4 else 3 if len(guess) == 5 else 54
    
  return sum(map(score_guess, guesses))

