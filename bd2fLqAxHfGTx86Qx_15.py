
def can_complete(initial, word):
  for i in initial:
    if i not in word:
      return False
  word_same_letters = ""
  for i in word:
    if i in initial:
      word_same_letters += i
  word_same_amount_letters = ""
  for i in word_same_letters:
    if i not in word_same_amount_letters:
      word_same_amount_letters += i
  return word_same_amount_letters == initial

