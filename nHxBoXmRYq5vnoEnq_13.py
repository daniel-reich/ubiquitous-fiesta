
def vowels(string):
  if len(string) == 0: return 0
  if len(string) == 1: return 1 if string[0] in "aeiou" else 0
  return vowels(string[0]) + vowels(string[1:])

