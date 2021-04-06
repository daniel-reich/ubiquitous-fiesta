
def insert_whitespace(txt):
  k = ""
  for letter in txt:
    if letter.isupper():
      k += " "
    k += letter
  return k[1:]

