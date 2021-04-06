
# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
  vowels = "aeiou"
  for x in string:
    if x in vowels:
      nstring=string.replace(x, "")
      string=nstring
  return nstring

