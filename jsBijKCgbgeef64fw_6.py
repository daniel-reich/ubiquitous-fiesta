
def wumbo(words):
  for letter in words:
    if letter == "M":
      words = words.replace(letter,"W")
  return words

