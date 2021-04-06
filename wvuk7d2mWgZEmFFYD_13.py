
def shared_letters(txt1, txt2):
  counter = 0
  for ch in set(txt1):
    if ch in txt2:
      counter += 1
  return counter

