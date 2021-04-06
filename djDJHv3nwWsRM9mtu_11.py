
def validate_spelling(txt):
  return ''.join(l[0] for l in txt.split()[:-1])==txt.split()[-1][:-1].upper()

