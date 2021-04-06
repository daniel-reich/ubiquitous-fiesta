
# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
  vowels = "aeiou"
  for i in range(len(vowels)):
    string = string.replace(vowels[i], "")
  return string

