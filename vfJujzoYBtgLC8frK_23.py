
def word_to_decimal(word):
  base = "abcdefghijklmnopqrstuvwxyz".index(max(word.lower()))+11
  return int(word.lower(),base)

