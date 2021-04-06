
def word_builder(letters, positions):
  final = [' ']*len(letters)
  for l,n in zip(letters,positions):
    final[n]=l
  return ''.join(final)

