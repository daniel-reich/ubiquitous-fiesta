
def get_middle(word):
  if not word:
    return word
  elif not len(word) % 2:
    return word[(len(word)//2) -1] + word[len(word)//2]
  else:
    return word[len(word)//2]

