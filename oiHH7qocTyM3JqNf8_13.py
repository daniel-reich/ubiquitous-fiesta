
def move(word):
  lst = []
  word = list(word)
  for i in word:
    lst.append(chr(ord(i)+1))
  return ''.join(lst)

