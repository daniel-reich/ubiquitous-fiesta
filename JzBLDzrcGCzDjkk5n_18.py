
def encrypt(word):
  reverse_word= word[::-1]
  print(word,"word")
  print(reverse_word,"reverse_word")
  reverse_word=reverse_word.replace("a","0")
  reverse_word=reverse_word.replace("e","1")
  reverse_word=reverse_word.replace("o","2")
  reverse_word=reverse_word.replace("u","3")
  reverse_word+="aca"
  print(reverse_word,"reverse_word")
  return reverse_word

