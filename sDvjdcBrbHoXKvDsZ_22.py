
def anagram(name, words):
  name = list(name.lower().replace(' ',''))
  for word in words:
    for letter in word.lower():
      try:
        name.pop(name.index(letter))
      except:
        return False
  
  if len(name) == 0:
    return True
  else:
    return False

