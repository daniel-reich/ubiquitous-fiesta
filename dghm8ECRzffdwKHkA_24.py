
def capital_letters(txt):
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  count = 0
  for i in txt:
    if i in letters:
      count += 1
  return count

