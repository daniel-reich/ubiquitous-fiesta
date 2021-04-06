
def increasing_word_weights(sentence):
  punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  sentence = sentence.translate(str.maketrans('', '', punctuation))
  weight = 0
  weight2 = 0
  for word in sentence.split():
    for i in word:
      weight += ord(i)
    if weight > weight2:
      weight2 = weight
      weight = 0
    else:
      return False
  return True

