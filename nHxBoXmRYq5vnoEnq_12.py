
def vowels(string):
  if not string:
    return 0
  return (1 if string[0] in "aeiou" else 0) + vowels(string[1:])

