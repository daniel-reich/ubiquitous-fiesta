
def caesar_cipher(text, key):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  return ''.join(alphabet[(alphabet.find(ch)+key)%26] if ch in alphabet else ch for ch in text)

