
def no_duplicate_letters(phrase):
  noDups = True
  words = phrase.split(" ")
  print(words)
  for word in words:
    if not noDups:
      break
    previouslyUsed = []
    for letter in word:
      if letter in previouslyUsed:
        noDups = False
        break
      previouslyUsed.append(letter)
  return noDups

