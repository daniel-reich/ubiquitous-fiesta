
def retrieve(txt):
  vowels = ["a", "e", "i", "o", "u", "y"]
  output = list()
  for word in txt.lower().strip(".").split():
    for vowel in vowels:
      if word.startswith(vowel):
        output.append(word)
  return output

