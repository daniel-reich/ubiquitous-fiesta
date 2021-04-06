
def increasing_word_weights(sentence):
  clean = ''.join(i for i in sentence if i.isalpha() or i in ' ')
  value = [sum(ord(letter) for letter in word) for word in clean.split()]
  return value == sorted(value)

