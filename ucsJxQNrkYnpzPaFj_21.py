
def char_appears(sentence, char):
  charAppearsList = []
  words = sentence.split(" ")
  for word in words:
    count = 0
    for letter in word.lower():
     if letter == char.lower():
      count = count + 1
    charAppearsList.append(count)
  return charAppearsList

