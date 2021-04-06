
def get_middle(word):
  try:
    if len(word) % 2 == 0:
      return word[len(word)//2 - 1] + word[len(word)//2]
    else:
      return word[len(word)//2]
  except IndexError:
    return ''

