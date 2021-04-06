
def in_alpha(word):
  sum = 0
  word = word.lower()
  for w in word:
    if w in "abcdefghijklmnopqrstuvwxyz":
      sum += ord(w)
  if sum % 2 == 0:
    return True
  else:
    return False

