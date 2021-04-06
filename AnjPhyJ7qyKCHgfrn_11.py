
# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
  retval = ''
  for char in string:
    if char.lower() not in 'aeiou':
      retval += char
  return retval

