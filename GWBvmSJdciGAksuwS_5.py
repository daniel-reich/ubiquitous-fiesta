
def find_letters(word):
  return [i for i in list(word) if list(word).count(i) < 2]

