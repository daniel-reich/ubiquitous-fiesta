
def count_claps(txt):
  counter = 0
  for char in txt:
    if char == 'C':
      counter += 1
  return counter

