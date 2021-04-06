
def num(word):
  values = [ord(x) for x in word if x.isalpha()]
  return sum(values)
  
def increasing_word_weights(sentence):
  words = sentence.split(" ")
  values = [num(word) for word in words]
  return values == sorted(values)

