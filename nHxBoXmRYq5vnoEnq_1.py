
def vowels(string):
  if string == "": return 0
  return 1*(string[0] in "aeiou") + vowels(string[1:])

