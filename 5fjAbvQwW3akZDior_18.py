
def unrepeated(txt):
  new_string = ""
  for letter in txt:
    if letter not in new_string:
      new_string += letter
  return new_string

