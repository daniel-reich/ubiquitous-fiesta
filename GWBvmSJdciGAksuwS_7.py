
def find_letters(word):
  u = []
  for char in word:
    if word.count(char) < 2:
      u.append(char)
  return u

