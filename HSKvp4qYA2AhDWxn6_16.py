
def total_points(guesses, word):
  total_points = 0
  for guess in guesses:
    print(guess)
    total_points += get_points(guess, word)
  return total_points
  
def get_points(guess, word):
  w = list(word)
  for letter in guess:
    if letter in w:
      w.remove(letter)
    else:
      return 0
  if len(guess) >= 6:
    return 54
  else:
    return len(guess) - 2

