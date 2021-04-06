
alphabet = "abcdefghijlmnopqrstuvwxyz"
def tap_code(text):
  print(text)
  if "." in text:
    result = translate_to_words(text)
  else:
    result = translate_to_code(text)
  return result
​
def translate_to_words(code):
  word = ""
  segments = code.split()
  coded_letters = []
  for i in range(int(len(segments)/2)):
    row_points = segments[i * 2]
    collumn_points = segments[i * 2 + 1]
    coded_letters.append([len(row_points), len(collumn_points)])
  for coded_letter in coded_letters:
    position = (coded_letter[0] - 1) * 5 + coded_letter[1] - 1
    letter = alphabet[position]
    word += letter
  return word
​
def translate_to_code(text):
  code = ""
  words = text.lower().replace("k", "c").split()
  for word in words:
    for letter in word:
      letter_pos = alphabet.find(letter)
      row = letter_pos // 5 + 1
      collumn = letter_pos % 5 + 1
      for i in range(row):
        code += "."
      code += " "
      for i in range(collumn):
        code += "."
      code += " "
  return (code[:-1])

