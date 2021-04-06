
def is_smooth(sentence):
  sentence = sentence.lower().split(' ')
  for i in range(len(sentence) - 1):
    word = sentence[i]
    next_word = sentence[i + 1]
    if word[-1] != next_word[0]:
      return False
  return True

