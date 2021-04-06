
def hangman(phrase, lst):
  fin,letters = [],'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for x in phrase:
    if x.lower() not in lst and x in letters: fin.append('-')
    else: fin.append(x)
  return ''.join(fin)

