
def camelCasing(txt):
  words = txt.replace("_", " ").split()
  return words[0].lower() + "".join(map(str.capitalize, words[1:]))

