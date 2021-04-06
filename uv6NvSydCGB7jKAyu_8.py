
def is_parsel_tongue(sentence):
  cap = sentence.upper().split()
  for word in cap:
    if 'S' in word:
      if 'SS' not in word:
        return False
  return True

