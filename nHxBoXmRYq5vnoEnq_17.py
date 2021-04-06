
def vowels(string):
  return 0 if string == '' else 1+ vowels(string[1:]) if string[0] in 'aeiou' else 0 + vowels(string[1:])

