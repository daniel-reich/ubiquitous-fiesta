
def is_parsel_tongue(sentence):
  for i in sentence.split(' '):
    if ('s' in i.lower()) and ('ss' not in i.lower()):
      return False
  return True

