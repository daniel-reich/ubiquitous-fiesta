
def find_nemo(sentence):
  sentance_lst = sentence.split(' ')
  try:
    return 'I found Nemo at {}!'.format(sentance_lst.index('Nemo')+1)
  except ValueError:
    return "I can't find Nemo :("

