
def can_find(bigrams, words):
  count = 0
  for chars in bigrams:
    for word in words:
      if chars in word:
        count += 1
    if count == 0:
      return False
    count = 0
  return True

