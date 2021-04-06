
def sort_word(word):
  #word = word.split()
  word = list(word)
  word.sort()
  final_word = ''
  for char in word:
    final_word = final_word + char
  return final_word

