
def sharedLetters(a, b):
  return ''.join(sorted(set(a.lower())&(set(b.lower()))))

