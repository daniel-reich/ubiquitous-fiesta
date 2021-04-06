
def flip(txt, spec):
  return ' '.join([x[::-1] if spec == "word" else x for x in txt.split()]) if spec == 'word' else ' '.join([x for x in txt.split()][::-1])

