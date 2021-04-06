
def true_alphabetic(txt):
  letters = sorted(c for c in txt.replace(' ', ''))
  for i, c in enumerate(txt):
    if c == ' ':
      letters.insert(i, ' ')
  return ''.join(letters)

