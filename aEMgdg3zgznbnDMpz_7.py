
def rotated_words(txt, x = 0):
  for word in set(txt.split(" ")):
    x += all(1 if c in "HIMNOSTUVWXYZ" else 0 for c in word)
  return x if txt else 0

