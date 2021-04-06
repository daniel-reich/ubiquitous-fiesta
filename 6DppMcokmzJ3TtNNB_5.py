
def true_alphabetic(txt):
  letters = iter(sorted(ch for ch in txt if ch != ' '))
  return ''.join(next(letters) if ch != ' ' else ch for ch in txt)

