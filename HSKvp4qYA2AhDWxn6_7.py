
def total_points(guesses, word):
  word_letters = {}
  for letter in word:
    if not letter in word_letters.keys():
      word_letters[letter] = 1
    else:
      word_letters[letter] = word_letters[letter] + 1
      
  score = 0
  
  
  for guess in guesses:
    current = {}
    valid = True
    for letter in guess:
      if letter in word:
        if not letter in current.keys():
          current[letter] = 1
        else:
          current[letter] = current[letter] + 1
        if current[letter] > word_letters[letter]:
          valid = False
          break
      else:
        valid = False
        break
    
    if valid:
      score += (-2 + len(guess))
      if len(guess) == 6:
        score += 50
  
  return score

