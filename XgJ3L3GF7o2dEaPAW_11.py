
def sharedLetters(a, b):
  return "".join(sorted(list(set(a.lower()).intersection(set(b.lower())))))

