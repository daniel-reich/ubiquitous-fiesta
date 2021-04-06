
def capital_letters(txt):
  count = 0
  for i in txt:
    if i == i.upper():
      count += 1
  return count

