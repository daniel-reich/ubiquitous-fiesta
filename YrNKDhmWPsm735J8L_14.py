
def sort_word(word):
  final_word = ""
  uppercase_string = ""
  lowercase_string = ""
  for i in word.split():
    if i == i.upper():
      uppercase_string += i
    else:
      lowercase_string += i
  for i in sorted(uppercase_string):
    final_word += i
  for i in sorted(lowercase_string):
    final_word += i
  return final_word

