
def find_nemo(sentence):
  split = sentence.split(' ')
  if 'Nemo' in split:
    return "I found Nemo at {}!".format(split.index('Nemo') + 1)
  else:
    return "I can't find Nemo :("

