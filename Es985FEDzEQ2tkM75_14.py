
def caesar_cipher(string, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return "".join([alphabet[(alphabet.index(letter) + key)%len(alphabet)] if letter.isalpha() else letter for letter in string  ]);

