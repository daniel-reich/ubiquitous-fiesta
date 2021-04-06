
def no_duplicate_letters(phrase):
  for word in phrase.split():
    temp = []
    for ch in word:
      if ch not in temp:
        temp.append(ch)
      else:
        return False
  return True

