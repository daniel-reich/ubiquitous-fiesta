
def sharedLetters(a, b):
  return "".join(sorted(set([x for x in a.lower() if x in b.lower()])))

