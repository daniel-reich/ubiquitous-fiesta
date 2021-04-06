
# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
  vowels = "aeiou"
  return "".join([ele for ele in list(string) if ele not in vowels])

