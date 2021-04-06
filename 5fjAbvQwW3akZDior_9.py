
def unrepeated(txt):
  letters = []
  for i in txt:
    if i not in letters:
      letters.append(i)
  return ''.join(letters)

