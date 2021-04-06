
def move(word):
  moved_word = ''
  for i in word:
    moved_word += chr(ord(i) + 1)
  return moved_word

