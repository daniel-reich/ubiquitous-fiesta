
def total_points(guesses, word):
  score = 0
  for guess in guesses:
    count = 0
    wordr = list(word)
    for letter in guess:
      if letter not in wordr:
        count = 0
        break
      if letter in wordr:
        wordr.remove(letter)
        count += 1
    if count == 3:
      score += 1
    if count == 4:
      score += 2
    if count == 5:
      score += 3
    if count == 6:
      score += 54
    wordr = list(word)      
  return score

