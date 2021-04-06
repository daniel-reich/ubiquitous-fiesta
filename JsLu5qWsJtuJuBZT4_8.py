
def flip(txt, spec):
  if len(txt.split())>1:
    if spec=='word':
      return ' '.join(x[::-1] for x in txt.split())
    return ' '.join(x for x in txt.split()[::-1])
  return txt[::-1] if spec=='word' else txt

