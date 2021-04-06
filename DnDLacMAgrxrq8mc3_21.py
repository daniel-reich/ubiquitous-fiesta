
def blah_blah(txt, n):
  words = txt.split()
  return ' '.join(w if i < len(words) - n else 'blah' for i,w in enumerate(words))+'...'

