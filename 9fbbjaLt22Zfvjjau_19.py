
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def paul_cipher(txt):
  result = []; prev = 'Z'
  for letter in txt.upper():
    if letter in alphabet:
      idx = (alphabet.index(letter) + alphabet.index(prev) + 1) % 26
      result.append(alphabet[idx])
      prev = letter
    else:
      result.append(letter)
  return ''.join(result)

