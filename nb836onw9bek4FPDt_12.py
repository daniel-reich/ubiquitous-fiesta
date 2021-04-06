
def count_same_ends(txt):
  def validator(word):
    return len(word) > 1
  def correction(word):
    correct = ''
    incorrect = list('!.,;@!%^')
    
    for l8r in word:
      if l8r not in incorrect:
        correct += l8r
    
    return correct
  def compare(word):
    return word[0].lower() == word[-1].lower()
  
  words = txt.split()
  valid = []
  
  for word in words:
    if validator(word) == True:
      valid.append(word)
  
  correct = []
  
  for word in valid:
    correct.append(correction(word))
  
  count = 0
  
  for word in correct:
    if compare(word) == True:
      count += 1
  
  return count

