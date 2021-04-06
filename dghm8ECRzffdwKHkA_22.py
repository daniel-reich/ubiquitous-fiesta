
def capital_letters(txt):
  count = 0
  for x in txt:
    if x == x.capitalize():
      count += 1
  return count

