
def find_letters(word):
  lst = [l for l in word if word.count(l) <= 1]
  return lst

