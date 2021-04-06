
def find_nemo(sentence):
  lst = [word for word in sentence.split()]
  try:
    ndx = lst.index('Nemo') + 1
    return 'I found Nemo at {}!'.format(ndx)
  except:
    return "I can't find Nemo :("

