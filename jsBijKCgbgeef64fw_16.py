
def wumbo(words):
  translation = ""
  for letter in words:
    if letter == "M":
      translation = translation + "W"
    else:
      translation = translation + letter
  return translation

