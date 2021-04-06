
def sort_word(word):
  word_list = list(word)
  word_list.sort()
  final_word = ""
  
  for char in word_list:
    final_word = final_word + char
  
  return final_word

