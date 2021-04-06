
def caesar_cipher(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  ting = ''
  for i in text:
    if i in alphabet:
      ind = alphabet.find(i)+key
      if ind>25:
        ind -= 26
      ting+=alphabet[ind]
    else:
      ting+=i
  return ting

