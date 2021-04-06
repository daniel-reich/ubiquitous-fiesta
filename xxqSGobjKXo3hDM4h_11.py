
def ing_extractor(string):
  def is_valid_ing(word):
    
    word = word.lower()
    if 'ing' in word:
      if len(word) <= 5 or word == 'string':
        return False
      else:
        return True
    else:
      return False
  
  words = string.split()
  valid = []
  
  for word in words:
    if is_valid_ing(word) == True:
      valid.append(word)
  
  return valid

