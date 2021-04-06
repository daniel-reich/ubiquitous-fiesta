
def char_appears(sentence, char):
  result = []
  divided = sentence.split(" ")
  for word in divided:
    result.append(word.lower().count(char))
  return result

