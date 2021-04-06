
def increasing_word_weights(sentence):
  res = [sum(ord(ch) for ch in word if ch.isalpha()) for word in sentence.split()]
  return res == sorted(res)

