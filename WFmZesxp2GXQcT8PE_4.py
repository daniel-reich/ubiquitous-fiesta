
def digital_cipher(message, key):
  number = tuple(map(int, str(key)))
  length = len(number)
  return [
    ord(letter) - 96 + number[index % length]
    for index, letter in enumerate(message)
  ]
  
digitalCipher = digital_cipher

