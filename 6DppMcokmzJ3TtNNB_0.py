
def true_alphabetic(txt):
  letters = iter(sorted(txt.replace(' ', '')))
  return ''.join(' ' if i is ' ' else next(letters) for i in txt)

