
def can_complete(initial, word):
  initialIndices = []
  for letter in initial:
    if letter not in word:
      return False
    if initial.count(letter) > word.count(letter):
      return False
  for i in range(0, len(initial)):
    initialIndices.append(word.index(initial[i])) 
  if initialIndices != sorted(initialIndices):
    return False
  return True

