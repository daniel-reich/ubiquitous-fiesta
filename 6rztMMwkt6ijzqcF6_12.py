
def is_repeated(txt):
  return next((24//i for i in range(1, 13) if txt == txt[:i] * (24//i)), False)

