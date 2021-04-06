
from collections import Counter
​
​
def total_points(guesses, word):
  score = 0
  
  for guess in guesses:
    if Counter(guess) == Counter(word):
      score += 54
    elif Counter(guess) - Counter(word):
      continue
    else:
      score += len(guess) - 2
      
  return score

