
def camelCasing(txt):
  words = txt.replace('_', ' ').split()
  return ''.join(word.lower() if inx == 0
            else word.capitalize()
            for (inx, word) in enumerate(words))

