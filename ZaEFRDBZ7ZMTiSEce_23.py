
def find_nemo(sentence):
  words = sentence.split(' ')
  if ('Nemo' in words):
    return 'I found Nemo at ' + str(words.index('Nemo') + 1) +'!'
  return 'I can\'t find Nemo :('

