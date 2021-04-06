
def word_builder(letters, positions):
  ls=[None]*len(letters)
  for i in range(len(letters)):
    ls[positions[i]]=letters[i]
  return ''.join(ls)

