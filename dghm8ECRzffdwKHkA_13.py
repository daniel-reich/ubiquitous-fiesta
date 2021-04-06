
def capital_letters(txt):
  count = 0
  for letter in txt:
    if letter.isupper():
      count += 1
    
  return count

