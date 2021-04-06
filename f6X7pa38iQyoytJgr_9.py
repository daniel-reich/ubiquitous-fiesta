
def increasing_word_weights(sentence):
  last = 0
  for word in sentence.split(' '):
    weight = sum(ord(x) for x in word if x.isalpha())
    if weight < last: return False
    last = weight
  return True

