
def sum_of_vowels(sentence):
  point = {
    "A" :4,
    "E" :3,
    "I" :1,
    "O" :0,
    "U" :0
  }
  result = 0
  for n in range(len(sentence)):
    if sentence[n] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
      result += point.get(sentence[n].upper())
  return (result)

