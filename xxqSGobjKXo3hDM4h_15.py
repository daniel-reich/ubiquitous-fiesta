
def ing_extractor(string):
  vowels = "aeiouAEIOU*"
  result = []
  for word in string.split():
    if word[-3:].lower() == "ing":
      partial = word[:-3]
      for letter in partial:
        if letter in vowels:
          result.append(word)
          break
  return result

