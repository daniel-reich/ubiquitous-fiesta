
def get_missing_letters(s):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  alphabet_array = []
  input_array = []
  for char in alphabet:
    alphabet_array.append(char)
  for char in s:
    input_array.append(char)
  result = ''
  for char in sorted(set(alphabet_array) - set(input_array)):
    result += char
  return result

