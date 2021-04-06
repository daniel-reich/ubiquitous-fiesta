
def flip(txt, spec):
  return ' '.join([word[::-1] for word in txt.split()]) if spec =="word" else ' '.join(reversed(txt.split()))

