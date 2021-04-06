
def move(word):
  letters="abcdefghijklmnopqrstuvwxyz"
  new_word=""
  for x in word:
    i=letters.find(x)
    new_word+=letters[i+1]
  return new_word

