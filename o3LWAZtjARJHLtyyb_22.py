
def reverse_case(txt):
  return ''.join([letter.upper() if letter.islower() else letter.lower() for letter in txt])

