
def word_builder(letters, positions):
  a=[1]*len(letters)
  for i in range(len(letters)):
    a[positions[i]]=letters[i]
  return ''.join(a)

