
def shared_letters(txt1, txt2):
  count = 0
  for l8r in set(txt1):
    if l8r in txt2:
      count += 1
  return count

