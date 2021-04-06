
# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
  vowels = "aeiou"
  
  ns = ''
  for item in string:
    if item in vowels:
      continue
    else:
      ns += item
  
  return ns

