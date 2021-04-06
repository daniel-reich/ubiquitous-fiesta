
def sharedLetters(a, b):
  return ''.join(sorted(set([l for l in a.lower() if l in b.lower()]), key=str.lower))

