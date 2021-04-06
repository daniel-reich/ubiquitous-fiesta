
def get_missing_letters(s):
  output = 'abcdefghijklmnopqrstuvwxyz'
  for letter in s:
    output = output.replace(letter, '')
  return output

