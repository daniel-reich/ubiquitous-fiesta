
def move(word):
  final_string = ''
  word_2 = [ord(i)+1 for i in word]
  for i in word_2:
    final_string = final_string + chr(i)
  return final_string

